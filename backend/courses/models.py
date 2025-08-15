from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from accounts.models import User


class Category(models.Model):
    """Course categories."""
    name = models.CharField(_('name'), max_length=100, unique=True)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    description = models.TextField(_('description'), blank=True)
    icon = models.CharField(_('icon'), max_length=50, blank=True)  # FontAwesome icon class
    color = models.CharField(_('color'), max_length=7, default='#007bff')  # Hex color
    is_active = models.BooleanField(_('is active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Course(models.Model):
    """Course model."""
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)
    description = models.TextField(_('description'))
    short_description = models.CharField(_('short description'), max_length=300, blank=True)
    
    # Course details
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    level = models.CharField(
        _('level'),
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert'),
        ],
        default='beginner'
    )
    
    # Course content
    thumbnail = models.ImageField(_('thumbnail'), upload_to='course_thumbnails/', blank=True, null=True)
    preview_video = models.URLField(_('preview video'), blank=True)
    duration = models.PositiveIntegerField(_('duration in minutes'), default=0)
    total_lessons = models.PositiveIntegerField(_('total lessons'), default=0)
    
    # Course settings
    is_free = models.BooleanField(_('is free'), default=False)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, default=0.00)
    is_published = models.BooleanField(_('is published'), default=False)
    is_featured = models.BooleanField(_('is featured'), default=False)
    is_active = models.BooleanField(_('is active'), default=True)
    
    # Course statistics
    enrolled_students = models.PositiveIntegerField(_('enrolled students'), default=0)
    enrollment_count = models.PositiveIntegerField(_('enrollment count'), default=0)
    rating = models.DecimalField(
        _('rating'), 
        max_digits=3, 
        decimal_places=2, 
        default=0.00,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    total_ratings = models.PositiveIntegerField(_('total ratings'), default=0)
    
    # SEO and metadata
    meta_title = models.CharField(_('meta title'), max_length=60, blank=True)
    meta_description = models.CharField(_('meta description'), max_length=160, blank=True)
    keywords = models.TextField(_('keywords'), blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(_('published at'), blank=True, null=True)
    
    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.meta_title:
            self.meta_title = self.title
        if not self.meta_description:
            self.meta_description = self.short_description or self.description[:160]
        super().save(*args, **kwargs)
    
    @property
    def average_rating(self):
        if self.total_ratings == 0:
            return 0
        return round(self.rating / self.total_ratings, 2)
    
    @property
    def is_popular(self):
        return self.enrolled_students > 100
    
    def get_absolute_url(self):
        return f'/courses/{self.slug}/'


class Lesson(models.Model):
    """Individual lesson within a course."""
    title = models.CharField(_('title'), max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    order = models.PositiveIntegerField(_('order'), default=0)
    
    # Lesson content
    content = models.TextField(_('content'), blank=True)
    video_url = models.URLField(_('video url'), blank=True)
    duration = models.PositiveIntegerField(_('duration in minutes'), default=0)
    
    # Lesson settings
    is_free = models.BooleanField(_('is free'), default=False)
    is_published = models.BooleanField(_('is published'), default=True)
    is_active = models.BooleanField(_('is active'), default=True)
    
    # Lesson resources
    resources = models.JSONField(_('resources'), default=list, blank=True)  # List of file URLs
    attachments = models.JSONField(_('attachments'), default=list, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('lesson')
        verbose_name_plural = _('lessons')
        ordering = ['course', 'order']
        unique_together = ['course', 'order']
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.order:
            last_lesson = Lesson.objects.filter(course=self.course).order_by('-order').first()
            self.order = (last_lesson.order + 1) if last_lesson else 1
        super().save(*args, **kwargs)


class CourseEnrollment(models.Model):
    """Track student enrollment in courses."""
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    # Progress tracking
    progress = models.PositiveIntegerField(
        _('progress percentage'), 
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    last_accessed = models.DateTimeField(auto_now=True)
    
    # Certificate
    certificate_issued = models.BooleanField(default=False)
    certificate_issued_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name = _('course enrollment')
        verbose_name_plural = _('course enrollments')
        unique_together = ['student', 'course']
        ordering = ['-enrolled_at']
    
    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"
    
    @property
    def is_completed(self):
        return self.progress == 100 and self.completed_at is not None


class CourseRating(models.Model):
    """Course ratings and reviews."""
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_ratings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(
        _('rating'),
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField(_('review'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('course rating')
        verbose_name_plural = _('course ratings')
        unique_together = ['student', 'course']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.student.username} rated {self.course.title} with {self.rating} stars"


class LessonProgress(models.Model):
    """Track student progress through individual lessons."""
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progress')
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    watch_time = models.PositiveIntegerField(_('watch time in seconds'), default=0)
    last_accessed = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('lesson progress')
        verbose_name_plural = _('lesson progress')
        unique_together = ['student', 'lesson']
        ordering = ['lesson__order']
    
    def __str__(self):
        status = "completed" if self.is_completed else "in progress"
        return f"{self.student.username} - {self.lesson.title} ({status})"


class CourseCertificate(models.Model):
    """Certificates issued upon course completion."""
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates')
    enrollment = models.OneToOneField(CourseEnrollment, on_delete=models.CASCADE, related_name='certificate')
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_number = models.CharField(_('certificate number'), max_length=50, unique=True)
    
    class Meta:
        verbose_name = _('course certificate')
        verbose_name_plural = _('course certificates')
        unique_together = ['student', 'course']
        ordering = ['-issued_at']
    
    def __str__(self):
        return f"Certificate for {self.student.username} - {self.course.title}"
    
    def save(self, *args, **kwargs):
        if not self.certificate_number:
            import uuid
            self.certificate_number = f"CERT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
