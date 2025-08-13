from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    # Video management
    path('', views.VideoListView.as_view(), name='video-list'),
    path('<int:pk>/', views.VideoDetailView.as_view(), name='video-detail'),
    path('create/', views.VideoCreateView.as_view(), name='video-create'),
    path('<int:pk>/edit/', views.VideoUpdateView.as_view(), name='video-update'),
    path('<int:pk>/delete/', views.VideoDeleteView.as_view(), name='video-delete'),
    
    # Video streaming
    path('<int:pk>/stream/', views.VideoStreamView.as_view(), name='video-stream'),
    path('<int:pk>/stream/start/', views.VideoStreamStartView.as_view(), name='video-stream-start'),
    path('<int:pk>/stream/end/', views.VideoStreamEndView.as_view(), name='video-stream-end'),
    
    # Video progress
    path('<int:pk>/progress/', views.VideoProgressView.as_view(), name='video-progress'),
    path('<int:pk>/progress/update/', views.VideoProgressUpdateView.as_view(), name='video-progress-update'),
    
    # Video comments
    path('<int:pk>/comments/', views.VideoCommentListView.as_view(), name='video-comments'),
    path('<int:pk>/comments/create/', views.VideoCommentCreateView.as_view(), name='video-comment-create'),
    path('comments/<int:pk>/edit/', views.VideoCommentUpdateView.as_view(), name='video-comment-update'),
    path('comments/<int:pk>/delete/', views.VideoCommentDeleteView.as_view(), name='video-comment-delete'),
    
    # Video bookmarks
    path('<int:pk>/bookmarks/', views.VideoBookmarkListView.as_view(), name='video-bookmarks'),
    path('<int:pk>/bookmarks/create/', views.VideoBookmarkCreateView.as_view(), name='video-bookmark-create'),
    path('bookmarks/<int:pk>/delete/', views.VideoBookmarkDeleteView.as_view(), name='video-bookmark-delete'),
    
    # Video analytics
    path('<int:pk>/analytics/', views.VideoAnalyticsView.as_view(), name='video-analytics'),
    path('analytics/summary/', views.VideoAnalyticsSummaryView.as_view(), name='video-analytics-summary'),
    
    # Video processing
    path('<int:pk>/process/', views.VideoProcessView.as_view(), name='video-process'),
    path('<int:pk>/status/', views.VideoProcessingStatusView.as_view(), name='video-processing-status'),
]
