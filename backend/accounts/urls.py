from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Authentication
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    
    # User profile
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/update/', views.UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/detail/', views.UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/picture/', views.update_profile_picture, name='profile-picture'),
    
    # Password management
    path('password/change/', views.PasswordChangeView.as_view(), name='password-change'),
    path('password/reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    
    # User activities
    path('activities/', views.UserActivityListView.as_view(), name='activities'),
    
    # User management (for admin/instructors)
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    
    # Current user
    path('me/', views.current_user, name='current-user'),
]
