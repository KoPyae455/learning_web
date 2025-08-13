from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.conf import settings
from courses.models import Lesson
from accounts.models import User
import os


def video_upload_path(instance, filename):
    """Generate upload path for video files."""
    return f'videos/{instance.lesson.course.slug}/{instance.lesson.order}_{filename}'


class Video(models.Model):
    """Video model for storing video information and files."""
    title = models.CharField(_('title'), max_length=200)
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='video')
    
    # Video file
    video_file = models.FileField(
        _('video file'),
        upload_to=video_upload_path,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'webm'])]
    )
    
    # Video metadata
    duration = models.PositiveIntegerField(_('duration in seconds'), default=0)
    file_size = models.PositiveBigIntegerField(_('file size in bytes'), default=0)
    resolution = models.CharField(_('resolution'), max_length=20, blank=True)  # e.g., "1920x1080"
    format = models.CharField(_('format'), max_length=10, blank=True)  # e.g., "mp4"
    
    # Video processing
    is_processed = models.BooleanField(_('is processed'), default=False)
    processing_status = models.CharField(
        _('processing status'),
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('processing', 'Processing'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
        ],
        default='pending'
    )
    processing_error = models.TextField(_('processing error'), blank=True)
    
    # Video settings
    is_public = models.BooleanField(_('is public'), default=True)
    allow_download = models.BooleanField(_('allow download'), default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    processed_at = models.DateTimeField(_('processed at'), blank=True, null=True)
    
    class Meta:
        verbose_name = _('video')
        verbose_name_plural = _('videos')
        ordering = ['lesson__order']
    
    def __str__(self):
        return f"{self.lesson.course.title} - {self.title}"
    
    def save(self, *args, **kwargs):
        if self.video_file and not self.file_size:
            self.file_size = self.video_file.size
        if self.video_file and not self.format:
            self.format = os.path.splitext(self.video_file.name)[1][1:].lower()
        super().save(*args, **kwargs)
    
    @property
    def file_size_mb(self):
        """Return file size in MB."""
        return round(self.file_size / (1024 * 1024), 2)
    
    @property
    def duration_formatted(self):
        """Return duration in MM:SS format."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def get_video_url(self):
        """Get the URL for the video file."""
        if self.video_file:
            return self.video_file.url
        return None


class VideoStream(models.Model):
    """Track video streaming sessions."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_streams')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='streams')
    session_id = models.CharField(_('session id'), max_length=100, unique=True)
    
    # Streaming data
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    total_watch_time = models.PositiveIntegerField(_('total watch time in seconds'), default=0)
    current_position = models.PositiveIntegerField(_('current position in seconds'), default=0)
    
    # Device information
    user_agent = models.TextField(_('user agent'), blank=True)
    ip_address = models.GenericIPAddressField(_('ip address'), blank=True, null=True)
    
    # Streaming quality
    quality = models.CharField(
        _('quality'),
        max_length=20,
        choices=[
            ('auto', 'Auto'),
            ('1080p', '1080p'),
            ('720p', '720p'),
            ('480p', '480p'),
            ('360p', '360p'),
        ],
        default='auto'
    )
    
    class Meta:
        verbose_name = _('video stream')
        verbose_name_plural = _('video streams')
        ordering = ['-started_at']
    
    def __str__(self):
        return f"{self.user.username} streaming {self.video.title}"
    
    @property
    def is_active(self):
        return self.ended_at is None
    
    @property
    def watch_duration(self):
        """Calculate total watch duration."""
        if self.ended_at:
            return (self.ended_at - self.started_at).total_seconds()
        return 0


class VideoAnalytics(models.Model):
    """Track video analytics and metrics."""
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='analytics')
    date = models.DateField(_('date'), auto_now_add=True)
    
    # View counts
    total_views = models.PositiveIntegerField(_('total views'), default=0)
    unique_views = models.PositiveIntegerField(_('unique views'), default=0)
    
    # Watch time
    total_watch_time = models.PositiveIntegerField(_('total watch time in seconds'), default=0)
    average_watch_time = models.PositiveIntegerField(_('average watch time in seconds'), default=0)
    
    # Engagement
    completion_rate = models.DecimalField(
        _('completion rate'),
        max_digits=5,
        decimal_places=2,
        default=0.00,
        help_text='Percentage of viewers who completed the video'
    )
    
    # Device and platform data
    mobile_views = models.PositiveIntegerField(_('mobile views'), default=0)
    desktop_views = models.PositiveIntegerField(_('desktop views'), default=0)
    tablet_views = models.PositiveIntegerField(_('tablet views'), default=0)
    
    class Meta:
        verbose_name = _('video analytics')
        verbose_name_plural = _('video analytics')
        unique_together = ['video', 'date']
        ordering = ['-date']
    
    def __str__(self):
        return f"Analytics for {self.video.title} on {self.date}"
    
    @property
    def average_watch_percentage(self):
        """Calculate average watch percentage."""
        if self.total_views > 0 and self.video.duration > 0:
            return (self.average_watch_time / self.video.duration) * 100
        return 0


class VideoComment(models.Model):
    """Comments on videos."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_comments')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    content = models.TextField(_('content'))
    timestamp = models.PositiveIntegerField(_('timestamp in seconds'), blank=True, null=True)
    
    # Moderation
    is_approved = models.BooleanField(_('is approved'), default=True)
    is_flagged = models.BooleanField(_('is flagged'), default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('video comment')
        verbose_name_plural = _('video comments')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.video.title}"
    
    @property
    def is_reply(self):
        return self.parent_comment is not None
    
    @property
    def reply_count(self):
        return self.replies.count()


class VideoBookmark(models.Model):
    """User bookmarks for videos."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_bookmarks')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='bookmarks')
    timestamp = models.PositiveIntegerField(_('timestamp in seconds'), default=0)
    note = models.TextField(_('note'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('video bookmark')
        verbose_name_plural = _('video bookmarks')
        unique_together = ['user', 'video']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Bookmark by {self.user.username} on {self.video.title} at {self.timestamp}s"
    
    @property
    def timestamp_formatted(self):
        """Return timestamp in MM:SS format."""
        minutes = self.timestamp // 60
        seconds = self.timestamp % 60
        return f"{minutes:02d}:{seconds:02d}"
