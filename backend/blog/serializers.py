# backend/blog/serializers.py
from rest_framework import serializers
from .models import BlogPost, BlogCategory, BlogTag, BlogComment, BlogLike, BlogBookmark, BlogNewsletter

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'

class BlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLike
        fields = '__all__'

class BlogBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogBookmark
        fields = '__all__'

class BlogNewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogNewsletter
        fields = '__all__'

