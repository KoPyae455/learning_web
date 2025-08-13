from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import User, UserProfile, UserActivity


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password', 
            'password_confirm', 'user_type'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password_confirm': {'write_only': True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        # Create user profile
        UserProfile.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    """Serializer for user login."""
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password')
            if not user.is_active:
                raise serializers.ValidationError('User account is disabled')
            attrs['user'] = user
        else:
            raise serializers.ValidationError('Must include email and password')
        
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile."""
    user = serializers.StringRelatedField(read_only=True)
    completion_rate = serializers.ReadOnlyField()
    
    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'skill_level', 'learning_goals', 'interests',
            'total_courses_enrolled', 'total_courses_completed', 
            'total_learning_hours', 'certificates_earned', 'badges_earned',
            'completion_rate', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'total_courses_enrolled', 'total_courses_completed',
            'total_learning_hours', 'certificates_earned', 'badges_earned'
        ]


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user information."""
    profile = UserProfileSerializer(read_only=True)
    full_name = serializers.ReadOnlyField()
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'full_name',
            'bio', 'avatar', 'date_of_birth', 'phone_number', 'user_type',
            'website', 'linkedin', 'github', 'twitter', 'email_verified',
            'profile', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'email_verified', 'created_at', 'updated_at']


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating user information."""
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'bio', 'avatar', 'date_of_birth',
            'phone_number', 'website', 'linkedin', 'github', 'twitter'
        ]


class PasswordChangeSerializer(serializers.Serializer):
    """Serializer for password change."""
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(required=True)
    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError("New passwords don't match")
        return attrs
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect')
        return value


class UserActivitySerializer(serializers.ModelSerializer):
    """Serializer for user activities."""
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = UserActivity
        fields = [
            'id', 'user', 'activity_type', 'description', 'related_object_id',
            'related_object_type', 'timestamp'
        ]
        read_only_fields = ['id', 'user', 'timestamp']


class PasswordResetSerializer(serializers.Serializer):
    """Serializer for password reset request."""
    email = serializers.EmailField()
    
    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('No user found with this email address')
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    """Serializer for password reset confirmation."""
    token = serializers.CharField()
    new_password = serializers.CharField(validators=[validate_password])
    new_password_confirm = serializers.CharField()
    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs
