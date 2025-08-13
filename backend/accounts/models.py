from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom user model with extended fields."""
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(_('bio'), max_length=500, blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatars/', blank=True, null=True)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    phone_number = models.CharField(_('phone number'), max_length=15, blank=True)
    
    # User type
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    ]
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='student'
    )
    
    # Social media links
    website = models.URLField(_('website'), blank=True)
    linkedin = models.URLField(_('linkedin'), blank=True)
    github = models.URLField(_('github'), blank=True)
    twitter = models.URLField(_('twitter'), blank=True)
    
    # Email verification
    email_verified = models.BooleanField(_('email verified'), default=False)
    email_verification_token = models.CharField(max_length=100, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self):
        return self.email
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    @property
    def is_instructor(self):
        return self.user_type == 'instructor'


class UserProfile(models.Model):
    """Extended user profile information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Learning preferences
    preferred_languages = models.JSONField(default=list, blank=True)
    skill_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert'),
        ],
        default='beginner'
    )
    
    # Learning goals
    learning_goals = models.TextField(blank=True)
    interests = models.JSONField(default=list, blank=True)
    
    # Progress tracking
    total_courses_enrolled = models.PositiveIntegerField(default=0)
    total_courses_completed = models.PositiveIntegerField(default=0)
    total_learning_hours = models.PositiveIntegerField(default=0)
    
    # Certificates and achievements
    certificates_earned = models.PositiveIntegerField(default=0)
    badges_earned = models.PositiveIntegerField(default=0)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def completion_rate(self):
        """Calculate course completion rate."""
        if self.total_courses_enrolled == 0:
            return 0
        return (self.total_courses_completed / self.total_courses_enrolled) * 100


class UserActivity(models.Model):
    """Track user learning activities."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(
        max_length=50,
        choices=[
            ('course_enrolled', 'Course Enrolled'),
            ('course_completed', 'Course Completed'),
            ('video_watched', 'Video Watched'),
            ('quiz_taken', 'Quiz Taken'),
            ('certificate_earned', 'Certificate Earned'),
            ('badge_earned', 'Badge Earned'),
        ]
    )
    description = models.TextField()
    related_object_id = models.PositiveIntegerField(blank=True, null=True)
    related_object_type = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'User Activity'
        verbose_name_plural = 'User Activities'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type} at {self.timestamp}"
