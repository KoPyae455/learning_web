from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # Categories
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', views.CategoryDetailView.as_view(), name='category-detail'),
    
    # Courses
    path('', views.CourseListView.as_view(), name='course-list'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('create/', views.CourseCreateView.as_view(), name='course-create'),
    path('<slug:slug>/edit/', views.CourseUpdateView.as_view(), name='course-update'),
    path('<slug:slug>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),
    
    # Lessons
    path('<slug:course_slug>/lessons/', views.LessonListView.as_view(), name='lesson-list'),
    path('<slug:course_slug>/lessons/create/', views.LessonCreateView.as_view(), name='lesson-create'),
    path('<slug:course_slug>/lessons/<int:pk>/', views.LessonDetailView.as_view(), name='lesson-detail'),
    path('<slug:course_slug>/lessons/<int:pk>/edit/', views.LessonUpdateView.as_view(), name='lesson-update'),
    path('<slug:course_slug>/lessons/<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson-delete'),
    
    # Enrollments
    path('<slug:slug>/enroll/', views.CourseEnrollmentView.as_view(), name='course-enroll'),
    path('<slug:slug>/unenroll/', views.CourseUnenrollmentView.as_view(), name='course-unenroll'),
    path('<slug:slug>/progress/', views.CourseProgressView.as_view(), name='course-progress'),
    
    # Ratings and Reviews
    path('<slug:slug>/rate/', views.CourseRatingView.as_view(), name='course-rate'),
    path('<slug:slug>/reviews/', views.CourseReviewListView.as_view(), name='course-reviews'),
    
    # Certificates
    path('<slug:slug>/certificate/', views.CourseCertificateView.as_view(), name='course-certificate'),
    
    # Search and Filter
    path('search/', views.CourseSearchView.as_view(), name='course-search'),
    path('featured/', views.FeaturedCourseListView.as_view(), name='featured-courses'),
    path('popular/', views.PopularCourseListView.as_view(), name='popular-courses'),
]
