from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Video, VideoStream, VideoAnalytics, VideoComment, VideoBookmark


class VideoAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'lesson', 'format', 'duration_formatted', 'file_size_mb',
        'is_processed', 'processing_status', 'is_public', 'created_at'
    ]
    list_filter = [
        'is_processed', 'processing_status', 'is_public', 'allow_download', 'format', 'created_at'
    ]
    search_fields = ['title', 'lesson__title', 'lesson__course__title']
    readonly_fields = ['file_size', 'format', 'created_at', 'updated_at', 'processed_at']
    ordering = ['-created_at']
    
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('title', 'lesson')
        }),
        (_('Video File'), {
            'fields': ('video_file', 'duration', 'resolution', 'format')
        }),
        (_('Processing'), {
            'fields': ('is_processed', 'processing_status', 'processing_error', 'processed_at')
        }),
        (_('Settings'), {
            'fields': ('is_public', 'allow_download')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at')
        }),
    )


class VideoStreamAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'video', 'quality', 'started_at', 'ended_at', 'total_watch_time', 'is_active'
    ]
    list_filter = ['quality', 'started_at', 'ended_at', 'video']
    search_fields = ['user__username', 'video__title', 'session_id']
    readonly_fields = ['started_at', 'ended_at']
    ordering = ['-started_at']
    
    fieldsets = (
        (_('Stream Information'), {
            'fields': ('user', 'video', 'session_id')
        }),
        (_('Streaming Data'), {
            'fields': ('started_at', 'ended_at', 'total_watch_time', 'current_position')
        }),
        (_('Device Information'), {
            'fields': ('user_agent', 'ip_address')
        }),
        (_('Quality'), {
            'fields': ('quality',)
        }),
    )


class VideoAnalyticsAdmin(admin.ModelAdmin):
    list_display = [
        'video', 'date', 'total_views', 'unique_views', 'total_watch_time',
        'average_watch_time', 'completion_rate', 'mobile_views', 'desktop_views'
    ]
    list_filter = ['date', 'video']
    search_fields = ['video__title']
    readonly_fields = ['date']
    ordering = ['-date']
    
    fieldsets = (
        (_('Video Information'), {
            'fields': ('video', 'date')
        }),
        (_('View Counts'), {
            'fields': ('total_views', 'unique_views')
        }),
        (_('Watch Time'), {
            'fields': ('total_watch_time', 'average_watch_time')
        }),
        (_('Engagement'), {
            'fields': ('completion_rate',)
        }),
        (_('Device Data'), {
            'fields': ('mobile_views', 'desktop_views', 'tablet_views')
        }),
    )


class VideoCommentAdmin(admin.ModelAdmin):
    list_display = [
        'author', 'video', 'is_approved', 'is_flagged', 'is_reply', 'created_at'
    ]
    list_filter = ['is_approved', 'is_flagged', 'created_at', 'video']
    search_fields = ['author__username', 'video__title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        (_('Comment Information'), {
            'fields': ('post', 'author', 'parent_comment')
        }),
        (_('Content'), {
            'fields': ('content', 'timestamp')
        }),
        (_('Moderation'), {
            'fields': ('is_approved', 'is_flagged')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at')
        }),
    )


class VideoBookmarkAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'timestamp_formatted', 'note', 'created_at']
    list_filter = ['created_at', 'video']
    search_fields = ['user__username', 'video__title', 'note']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    fieldsets = (
        (_('Bookmark Information'), {
            'fields': ('user', 'video')
        }),
        (_('Bookmark Details'), {
            'fields': ('timestamp', 'note')
        }),
        (_('Timestamp'), {
            'fields': ('created_at',)
        }),
    )


admin.site.register(Video, VideoAdmin)
admin.site.register(VideoStream, VideoStreamAdmin)
admin.site.register(VideoAnalytics, VideoAnalyticsAdmin)
admin.site.register(VideoComment, VideoCommentAdmin)
admin.site.register(VideoBookmark, VideoBookmarkAdmin)
