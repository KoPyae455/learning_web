# backend/blog/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import BlogPost, BlogCategory, BlogTag, BlogComment, BlogLike, BlogBookmark, BlogNewsletter
from .serializers import (
    BlogPostSerializer, BlogCategorySerializer, BlogTagSerializer,
    BlogCommentSerializer, BlogLikeSerializer, BlogBookmarkSerializer, BlogNewsletterSerializer
)

class BlogPostListView(generics.ListAPIView):
    """List all blog posts."""
    queryset = BlogPost.objects.filter(status='published', is_active=True).order_by('-created_at')
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BlogPostDetailView(generics.RetrieveAPIView):
    """Retrieve a specific blog post."""
    queryset = BlogPost.objects.filter(status='published', is_active=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]

class BlogPostCreateView(generics.CreateAPIView):
    """Create a new blog post."""
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

class BlogPostUpdateView(generics.UpdateAPIView):
    """Update a blog post."""
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class BlogPostDeleteView(generics.DestroyAPIView):
    """Delete a blog post."""
    queryset = BlogPost.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class BlogCategoryListView(generics.ListAPIView):
    """List all blog categories."""
    queryset = BlogCategory.objects.filter(is_active=True).order_by('name')
    serializer_class = BlogCategorySerializer

class BlogCategoryDetailView(generics.RetrieveAPIView):
    """Retrieve a specific blog category."""
    queryset = BlogCategory.objects.filter(is_active=True)
    serializer_class = BlogCategorySerializer
    lookup_field = 'slug'

class BlogTagListView(generics.ListAPIView):
    """List all blog tags."""
    queryset = BlogTag.objects.filter(is_active=True).order_by('name')
    serializer_class = BlogTagSerializer

class BlogTagDetailView(generics.RetrieveAPIView):
    """Retrieve a specific blog tag."""
    queryset = BlogTag.objects.filter(is_active=True)
    serializer_class = BlogTagSerializer
    lookup_field = 'slug'

class BlogCommentListView(generics.ListAPIView):
    """List comments for a blog post."""
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_slug = self.kwargs['slug']
        return BlogComment.objects.filter(post__slug=post_slug, is_approved=True)

class BlogCommentCreateView(generics.CreateAPIView):
    """Create a comment on a blog post."""
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticated]

class BlogCommentUpdateView(generics.UpdateAPIView):
    """Update a blog comment."""
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticated]

class BlogCommentDeleteView(generics.DestroyAPIView):
    """Delete a blog comment."""
    queryset = BlogComment.objects.all()
    permission_classes = [IsAuthenticated]

class BlogPostLikeView(generics.CreateAPIView):
    """Like a blog post."""
    serializer_class = BlogLikeSerializer
    permission_classes = [IsAuthenticated]

class BlogPostUnlikeView(generics.DestroyAPIView):
    """Unlike a blog post."""
    queryset = BlogLike.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        post_slug = self.kwargs['slug']
        user = self.request.user
        return get_object_or_404(BlogLike, post__slug=post_slug, user=user)

class BlogPostBookmarkView(generics.CreateAPIView):
    """Bookmark a blog post."""
    serializer_class = BlogBookmarkSerializer
    permission_classes = [IsAuthenticated]

class BlogPostUnbookmarkView(generics.DestroyAPIView):
    """Remove bookmark from a blog post."""
    queryset = BlogBookmark.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        post_slug = self.kwargs['slug']
        user = self.request.user
        return get_object_or_404(BlogBookmark, post__slug=post_slug, user=user)

class BlogSearchView(generics.ListAPIView):
    """Search blog posts."""
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return BlogPost.objects.filter(
                status='published',
                is_active=True,
                title__icontains=query
            ).order_by('-created_at')
        return BlogPost.objects.filter(status='published', is_active=True).order_by('-created_at')

class FeaturedBlogPostListView(generics.ListAPIView):
    """List featured blog posts."""
    queryset = BlogPost.objects.filter(status='published', is_active=True, is_featured=True).order_by('-created_at')
    serializer_class = BlogPostSerializer

class NewsletterSubscribeView(generics.CreateAPIView):
    """Subscribe to newsletter."""
    serializer_class = BlogNewsletterSerializer

class NewsletterUnsubscribeView(generics.DestroyAPIView):
    """Unsubscribe from newsletter."""
    queryset = BlogNewsletter.objects.all()
    serializer_class = BlogNewsletterSerializer
