from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import User, UserProfile, UserActivity
from .serializers import (
    UserRegistrationSerializer, UserLoginSerializer, UserSerializer,
    UserUpdateSerializer, UserProfileSerializer, PasswordChangeSerializer,
    UserActivitySerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
)


class UserRegistrationView(generics.CreateAPIView):
    """User registration endpoint."""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        with transaction.atomic():
            user = serializer.save()
            
            # Log activity
            UserActivity.objects.create(
                user=user,
                activity_type='account_created',
                description='User account created successfully'
            )
        
        # Generate token for immediate login
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'message': 'User registered successfully',
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class UserLoginView(generics.GenericAPIView):
    """User login endpoint."""
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        login(request, user)
        
        # Generate or get token
        token, created = Token.objects.get_or_create(user=user)
        
        # Log activity
        UserActivity.objects.create(
            user=user,
            activity_type='user_login',
            description='User logged in successfully'
        )
        
        return Response({
            'message': 'Login successful',
            'user': UserSerializer(user).data,
            'token': token.key
        })


class UserLogoutView(generics.GenericAPIView):
    """User logout endpoint."""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        # Log activity before logout
        UserActivity.objects.create(
            user=request.user,
            activity_type='user_logout',
            description='User logged out'
        )
        
        logout(request)
        return Response({'message': 'Logout successful'})


class UserProfileView(generics.RetrieveUpdateAPIView):
    """User profile view and update."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user


class UserProfileUpdateView(generics.UpdateAPIView):
    """Update user profile information."""
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    """User profile detail view and update."""
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user.profile


class PasswordChangeView(generics.GenericAPIView):
    """Change user password."""
    serializer_class = PasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        
        # Log activity
        UserActivity.objects.create(
            user=user,
            activity_type='password_changed',
            description='User password changed successfully'
        )
        
        return Response({'message': 'Password changed successfully'})


class PasswordResetView(generics.GenericAPIView):
    """Request password reset."""
    serializer_class = PasswordResetSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        
        # Generate reset token (in production, send email)
        # For now, just return success message
        return Response({
            'message': 'Password reset email sent (check console in development)'
        })


class PasswordResetConfirmView(generics.GenericAPIView):
    """Confirm password reset."""
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # In production, validate token and reset password
        # For now, just return success message
        return Response({'message': 'Password reset successful'})


class UserActivityListView(generics.ListAPIView):
    """List user activities."""
    serializer_class = UserActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return UserActivity.objects.filter(user=self.request.user)


class UserListView(generics.ListAPIView):
    """List all users (for admin/instructors)."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_instructor:
            return User.objects.all()
        return User.objects.none()


class UserDetailView(generics.RetrieveAPIView):
    """Get specific user details."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_instructor:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def current_user(request):
    """Get current authenticated user."""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def update_profile_picture(request):
    """Update user profile picture."""
    if 'avatar' not in request.FILES:
        return Response(
            {'error': 'No image file provided'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = request.user
    user.avatar = request.FILES['avatar']
    user.save()
    
    # Log activity
    UserActivity.objects.create(
        user=user,
        activity_type='profile_updated',
        description='User profile picture updated'
    )
    
    return Response({
        'message': 'Profile picture updated successfully',
        'avatar_url': user.avatar.url
    })
