from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Blog posts
    path('', views.BlogPostListView.as_view(), name='post-list'),
    path('<slug:slug>/', views.BlogPostDetailView.as_view(), name='post-detail'),
    path('create/', views.BlogPostCreateView.as_view(), name='post-create'),
    path('<slug:slug>/edit/', views.BlogPostUpdateView.as_view(), name='post-update'),
    path('<slug:slug>/delete/', views.BlogPostDeleteView.as_view(), name='post-delete'),
    
    # Categories
    path('categories/', views.BlogCategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', views.BlogCategoryDetailView.as_view(), name='category-detail'),
    
    # Tags
    path('tags/', views.BlogTagListView.as_view(), name='tag-list'),
    path('tags/<slug:slug>/', views.BlogTagDetailView.as_view(), name='tag-detail'),
    
    # Comments
    path('<slug:slug>/comments/', views.BlogCommentListView.as_view(), name='comment-list'),
    path('<slug:slug>/comments/create/', views.BlogCommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', views.BlogCommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', views.BlogCommentDeleteView.as_view(), name='comment-delete'),
    
    # Likes and bookmarks
    path('<slug:slug>/like/', views.BlogPostLikeView.as_view(), name='post-like'),
    path('<slug:slug>/unlike/', views.BlogPostUnlikeView.as_view(), name='post-unlike'),
    path('<slug:slug>/bookmark/', views.BlogPostBookmarkView.as_view(), name='post-bookmark'),
    path('<slug:slug>/unbookmark/', views.BlogPostUnbookmarkView.as_view(), name='post-unbookmark'),
    
    # Search
    path('search/', views.BlogSearchView.as_view(), name='search'),
    
    # Featured posts
    path('featured/', views.FeaturedBlogPostListView.as_view(), name='featured-posts'),
    
    # Newsletter
    path('newsletter/subscribe/', views.NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
    path('newsletter/unsubscribe/', views.NewsletterUnsubscribeView.as_view(), name='newsletter-unsubscribe'),
]
