# backend/videos/serializers.py
from rest_framework import serializers
from .models import Video, VideoStream, VideoAnalytics, VideoComment, VideoBookmark

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class VideoStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoStream
        fields = '__all__'

class VideoAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoAnalytics
        fields = '__all__'

class VideoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoComment
        fields = '__all__'

class VideoBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoBookmark
        fields = '__all__'

