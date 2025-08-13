from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class BlogCategory(models.Model):
    """Blog post categories."""
    name = models.CharField(_('name'), max_length=100, unique=True)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    description = models.TextField(_('description'), blank=True)
    icon = models.CharField(_('icon'), max_length=50, blank=True)  # FontAwesome icon class
    color = models.CharField(_('color'), max_length=7, default='#28a745')  # Hex color
    is_active = models.BooleanField(_('is active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('blog category')
        verbose_name_plural = _('blog categories')
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'slug': self.slug})


class BlogTag(models.Model):
    """Blog post tags."""
    name = models.CharField(_('name'), max_length=50, unique=True)
    slug = models.SlugField(_('slug'), max_length=50, unique=True)
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('blog tag')
        verbose_name_plural = _('blog tags')
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:tag_detail', kwargs={'slug': self.slug})


class BlogPost(models.Model):
    """Blog post model."""
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(BlogTag, blank=True, related_name='posts')
    
    # Content
    content = models.TextField(_('content'))
    excerpt = models.TextField(_('excerpt'), max_length=500, blank=True)
    featured_image = models.ImageField(_('featured image'), upload_to='blog_images/', blank=True, null=True)
    
    # Post settings
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(_('is featured'), default=False)
    allow_comments = models.BooleanField(_('allow comments'), default=True)
    
    # SEO and metadata
    meta_title = models.CharField(_('meta title'), max_length=60, blank=True)
    meta_description = models.CharField(_('meta description'), max_length=160, blank=True)
    keywords = models.TextField(_('keywords'), blank=True)
    
    # Statistics
    views = models.PositiveIntegerField(_('views'), default=0)
    likes = models.PositiveIntegerField(_('likes'), default=0)
    comment_count = models.PositiveIntegerField(_('comment count'), default=0)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(_('published at'), blank=True, null=True)
    
    class Meta:
        verbose_name = _('blog post')
        verbose_name_plural = _('blog posts')
        ordering = ['-published_at', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.meta_title:
            self.meta_title = self.title
        if not self.meta_description:
            self.meta_description = self.excerpt or self.content[:160]
        if self.status == 'published' and not self.published_at:
            from django.utils import timezone
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
    
    def increment_views(self):
        """Increment view count."""
        self.views += 1
        self.save(update_fields=['views'])
    
    @property
    def is_published(self):
        return self.status == 'published'
    
    @property
    def reading_time(self):
        """Estimate reading time in minutes."""
        words_per_minute = 200
        word_count = len(self.content.split())
        return max(1, round(word_count / words_per_minute))


class BlogComment(models.Model):
    """Comments on blog posts."""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    content = models.TextField(_('content'))
    
    # Moderation
    is_approved = models.BooleanField(_('is approved'), default=True)
    is_flagged = models.BooleanField(_('is flagged'), default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('blog comment')
        verbose_name_plural = _('blog comments')
        ordering = ['created_at']
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    
    @property
    def is_reply(self):
        return self.parent_comment is not None
    
    @property
    def reply_count(self):
        return self.replies.count()


class BlogLike(models.Model):
    """User likes on blog posts."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_likes')
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='user_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('blog like')
        verbose_name_plural = _('blog likes')
        unique_together = ['user', 'post']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"


class BlogBookmark(models.Model):
    """User bookmarks for blog posts."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_bookmarks')
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='bookmarks')
    note = models.TextField(_('note'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('blog bookmark')
        verbose_name_plural = _('blog bookmarks')
        unique_together = ['user', 'post']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Bookmark by {self.user.username} on {self.post.title}"


class BlogView(models.Model):
    """Track blog post views."""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='view_records')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_views', null=True, blank=True)
    ip_address = models.GenericIPAddressField(_('ip address'), blank=True, null=True)
    user_agent = models.TextField(_('user agent'), blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('blog view')
        verbose_name_plural = _('blog views')
        ordering = ['-viewed_at']
    
    def __str__(self):
        viewer = self.user.username if self.user else f"Anonymous ({self.ip_address})"
        return f"{viewer} viewed {self.post.title}"


class BlogNewsletter(models.Model):
    """Blog newsletter subscriptions."""
    email = models.EmailField(_('email'), unique=True)
    is_active = models.BooleanField(_('is active'), default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name = _('blog newsletter')
        verbose_name_plural = _('blog newsletters')
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return self.email
