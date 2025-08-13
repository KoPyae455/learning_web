from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (
    BlogCategory, BlogTag, BlogPost, BlogComment, BlogLike, 
    BlogBookmark, BlogView, BlogNewsletter
)


class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    extra = 0
    fields = ['author', 'content', 'is_approved', 'created_at']
    readonly_fields = ['created_at']


class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'category', 'status', 'is_featured', 
        'views', 'likes', 'comment_count', 'created_at'
    ]
    list_filter = [
        'status', 'is_featured', 'category', 'author', 'created_at', 'published_at'
    ]
    search_fields = ['title', 'content', 'author__username', 'author__email']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views', 'likes', 'comment_count', 'created_at', 'updated_at']
    ordering = ['-created_at']
    inlines = [BlogCommentInline]
    
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('title', 'slug', 'author', 'category', 'tags')
        }),
        (_('Content'), {
            'fields': ('content', 'excerpt', 'featured_image')
        }),
        (_('Settings'), {
            'fields': ('status', 'is_featured', 'allow_comments')
        }),
        (_('SEO'), {
            'fields': ('meta_title', 'meta_description', 'keywords')
        }),
        (_('Statistics'), {
            'fields': ('views', 'likes', 'comment_count')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at', 'published_at')
        }),
    )


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = [
        'author', 'post', 'is_approved', 'is_flagged', 'is_reply', 'created_at'
    ]
    list_filter = ['is_approved', 'is_flagged', 'created_at', 'post']
    search_fields = ['author__username', 'post__title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        (_('Comment Information'), {
            'fields': ('post', 'author', 'parent_comment')
        }),
        (_('Content'), {
            'fields': ('content',)
        }),
        (_('Moderation'), {
            'fields': ('is_approved', 'is_flagged')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at')
        }),
    )


class BlogLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']
    list_filter = ['created_at', 'post']
    search_fields = ['user__username', 'post__title']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


class BlogBookmarkAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'note', 'created_at']
    list_filter = ['created_at', 'post']
    search_fields = ['user__username', 'post__title', 'note']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


class BlogViewAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'ip_address', 'viewed_at']
    list_filter = ['viewed_at', 'post']
    search_fields = ['post__title', 'user__username', 'ip_address']
    readonly_fields = ['viewed_at']
    ordering = ['-viewed_at']


class BlogNewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'subscribed_at', 'unsubscribed_at']
    list_filter = ['is_active', 'subscribed_at', 'unsubscribed_at']
    search_fields = ['email']
    readonly_fields = ['subscribed_at', 'unsubscribed_at']
    ordering = ['-subscribed_at']


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogTag, BlogTagAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(BlogLike, BlogLikeAdmin)
admin.site.register(BlogBookmark, BlogBookmarkAdmin)
admin.site.register(BlogView, BlogViewAdmin)
admin.site.register(BlogNewsletter, BlogNewsletterAdmin)
