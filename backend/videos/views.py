# backend/videos/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Video, VideoStream, VideoAnalytics, VideoComment, VideoBookmark
from .serializers import (
    VideoSerializer, VideoStreamSerializer, VideoAnalyticsSerializer,
    VideoCommentSerializer, VideoBookmarkSerializer
)

class VideoListView(generics.ListAPIView):
    """List all videos."""
    queryset = Video.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class VideoDetailView(generics.RetrieveAPIView):
    """Retrieve a specific video."""
    queryset = Video.objects.filter(is_active=True)
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class VideoCreateView(generics.CreateAPIView):
    """Create a new video."""
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

class VideoUpdateView(generics.UpdateAPIView):
    """Update a video."""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

class VideoDeleteView(generics.DestroyAPIView):
    """Delete a video."""
    queryset = Video.objects.all()
    permission_classes = [IsAuthenticated]

class VideoStreamView(generics.RetrieveAPIView):
    """Stream a video."""
    queryset = Video.objects.filter(is_active=True)
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

class VideoStreamStartView(generics.CreateAPIView):
    """Start video streaming session."""
    serializer_class = VideoStreamSerializer
    permission_classes = [IsAuthenticated]

class VideoStreamEndView(generics.UpdateAPIView):
    """End video streaming session."""
    queryset = VideoStream.objects.all()
    serializer_class = VideoStreamSerializer
    permission_classes = [IsAuthenticated]

class VideoProgressView(generics.RetrieveAPIView):
    """Get video progress for a user."""
    serializer_class = VideoStreamSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        video_id = self.kwargs['pk']
        user = self.request.user
        return get_object_or_404(VideoStream, video_id=video_id, user=user)

class VideoProgressUpdateView(generics.UpdateAPIView):
    """Update video progress."""
    queryset = VideoStream.objects.all()
    serializer_class = VideoStreamSerializer
    permission_classes = [IsAuthenticated]

class VideoCommentListView(generics.ListAPIView):
    """List comments for a video."""
    serializer_class = VideoCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        video_id = self.kwargs['pk']
        return VideoComment.objects.filter(video_id=video_id, is_active=True)

class VideoCommentCreateView(generics.CreateAPIView):
    """Create a comment on a video."""
    serializer_class = VideoCommentSerializer
    permission_classes = [IsAuthenticated]

class VideoCommentUpdateView(generics.UpdateAPIView):
    """Update a video comment."""
    queryset = VideoComment.objects.all()
    serializer_class = VideoCommentSerializer
    permission_classes = [IsAuthenticated]

class VideoCommentDeleteView(generics.DestroyAPIView):
    """Delete a video comment."""
    queryset = VideoComment.objects.all()
    permission_classes = [IsAuthenticated]

class VideoBookmarkListView(generics.ListAPIView):
    """List bookmarks for a video."""
    serializer_class = VideoBookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        video_id = self.kwargs['pk']
        user = self.request.user
        return VideoBookmark.objects.filter(video_id=video_id, user=user)

class VideoBookmarkCreateView(generics.CreateAPIView):
    """Create a bookmark for a video."""
    serializer_class = VideoBookmarkSerializer
    permission_classes = [IsAuthenticated]

class VideoBookmarkDeleteView(generics.DestroyAPIView):
    """Delete a video bookmark."""
    queryset = VideoBookmark.objects.all()
    permission_classes = [IsAuthenticated]

class VideoAnalyticsView(generics.RetrieveAPIView):
    """Get analytics for a specific video."""
    serializer_class = VideoAnalyticsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        video_id = self.kwargs['pk']
        return get_object_or_404(VideoAnalytics, video_id=video_id)

class VideoAnalyticsSummaryView(generics.ListAPIView):
    """Get analytics summary for all videos."""
    queryset = VideoAnalytics.objects.all()
    serializer_class = VideoAnalyticsSerializer
    permission_classes = [IsAuthenticated]

class VideoProcessView(generics.CreateAPIView):
    """Process a video."""
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Placeholder for video processing
        return Response({"message": "Video processing started"}, status=status.HTTP_200_OK)

class VideoProcessingStatusView(generics.RetrieveAPIView):
    """Get video processing status."""
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # Placeholder for processing status
        return Response({"status": "completed"}, status=status.HTTP_200_OK)

