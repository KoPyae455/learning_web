# backend/courses/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Category, Course, Lesson, CourseEnrollment, CourseRating
from .serializers import (
    CategorySerializer, CourseSerializer, LessonSerializer,
    CourseEnrollmentSerializer, CourseRatingSerializer
)

class CategoryListView(generics.ListAPIView):
    """List all active categories."""
    queryset = Category.objects.filter(is_active=True).order_by('name')
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    """Retrieve a specific category."""
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class CourseListView(generics.ListAPIView):
    """List all active courses."""
    queryset = Course.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveAPIView):
    """Retrieve a specific course."""
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer
    lookup_field = 'slug'

class CourseCreateView(generics.CreateAPIView):
    """Create a new course."""
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CourseUpdateView(generics.UpdateAPIView):
    """Update a course."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class CourseDeleteView(generics.DestroyAPIView):
    """Delete a course."""
    queryset = Course.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class LessonListView(generics.ListAPIView):
    """List lessons for a specific course."""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_slug = self.kwargs['course_slug']
        return Lesson.objects.filter(course__slug=course_slug, is_active=True)

class LessonCreateView(generics.CreateAPIView):
    """Create a new lesson."""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

class LessonDetailView(generics.RetrieveAPIView):
    """Retrieve a specific lesson."""
    queryset = Lesson.objects.filter(is_active=True)
    serializer_class = LessonSerializer

class LessonUpdateView(generics.UpdateAPIView):
    """Update a lesson."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

class LessonDeleteView(generics.DestroyAPIView):
    """Delete a lesson."""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class CourseEnrollmentView(generics.CreateAPIView):
    """Enroll in a course."""
    serializer_class = CourseEnrollmentSerializer
    permission_classes = [IsAuthenticated]

class CourseUnenrollmentView(generics.DestroyAPIView):
    """Unenroll from a course."""
    queryset = CourseEnrollment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        course_slug = self.kwargs['slug']
        user = self.request.user
        return get_object_or_404(CourseEnrollment, course__slug=course_slug, user=user)

class CourseProgressView(generics.RetrieveAPIView):
    """Get course progress for a user."""
    serializer_class = CourseEnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        course_slug = self.kwargs['slug']
        user = self.request.user
        return get_object_or_404(CourseEnrollment, course__slug=course_slug, user=user)

class CourseRatingView(generics.CreateAPIView):
    """Rate a course."""
    serializer_class = CourseRatingSerializer
    permission_classes = [IsAuthenticated]

class CourseReviewListView(generics.ListAPIView):
    """List reviews for a course."""
    serializer_class = CourseRatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_slug = self.kwargs['slug']
        return CourseRating.objects.filter(course__slug=course_slug)

class CourseCertificateView(generics.RetrieveAPIView):
    """Get course completion certificate."""
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        # Placeholder for certificate generation
        return Response({"message": "Certificate feature coming soon"}, status=status.HTTP_200_OK)

class CourseSearchView(generics.ListAPIView):
    """Search courses."""
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return Course.objects.filter(
                is_active=True,
                title__icontains=query
            ).order_by('-created_at')
        return Course.objects.filter(is_active=True).order_by('-created_at')

class FeaturedCourseListView(generics.ListAPIView):
    """List featured courses."""
    queryset = Course.objects.filter(is_active=True, is_featured=True).order_by('-created_at')
    serializer_class = CourseSerializer

class PopularCourseListView(generics.ListAPIView):
    """List popular courses."""
    queryset = Course.objects.filter(is_active=True).order_by('-enrollment_count', '-created_at')
    serializer_class = CourseSerializer
