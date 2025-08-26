# from django.contrib import admin
# from django.utils.translation import gettext_lazy as _
# from .models import Category, Course, Lesson, CourseEnrollment, CourseRating, LessonProgress, CourseCertificate


# class LessonInline(admin.TabularInline):
#     model = Lesson
#     extra = 1
#     fields = ['title', 'order', 'duration', 'is_free', 'is_published']


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'is_active', 'created_at']
#     list_filter = ['is_active', 'created_at']
#     search_fields = ['name', 'description']
#     prepopulated_fields = {'slug': ('name',)}
#     ordering = ['name']


# class CourseAdmin(admin.ModelAdmin):
#     list_display = [
#         'title', 'instructor', 'category', 'level', 'is_published', 
#         'is_featured', 'enrolled_students', 'rating', 'created_at'
#     ]
#     list_filter = [
#         'is_published', 'is_featured', 'level', 'category', 'instructor', 'created_at'
#     ]
#     search_fields = ['title', 'description', 'instructor__username', 'instructor__email']
#     prepopulated_fields = {'slug': ('title',)}
#     readonly_fields = ['enrolled_students', 'rating', 'total_ratings', 'created_at', 'updated_at']
#     ordering = ['-created_at']
#     inlines = [LessonInline]
    
#     fieldsets = (
#         (_('Basic Information'), {
#             'fields': ('title', 'slug', 'description', 'short_description', 'instructor', 'category', 'level')
#         }),
#         (_('Content'), {
#             'fields': ('thumbnail', 'preview_video', 'duration', 'total_lessons')
#         }),
#         (_('Settings'), {
#             'fields': ('is_free', 'price', 'is_published', 'is_featured')
#         }),
#         (_('SEO'), {
#             'fields': ('meta_title', 'meta_description', 'keywords')
#         }),
#         (_('Statistics'), {
#             'fields': ('enrolled_students', 'rating', 'total_ratings')
#         }),
#         (_('Timestamps'), {
#             'fields': ('created_at', 'updated_at', 'published_at')
#         }),
#     )


# class LessonAdmin(admin.ModelAdmin):
#     list_display = ['title', 'course', 'order', 'duration', 'is_free', 'is_published', 'created_at']
#     list_filter = ['is_published', 'is_free', 'course', 'created_at']
#     search_fields = ['title', 'course__title']
#     ordering = ['course', 'order']
    
#     fieldsets = (
#         (_('Basic Information'), {
#             'fields': ('title', 'course', 'order')
#         }),
#         (_('Content'), {
#             'fields': ('content', 'video_url', 'duration')
#         }),
#         (_('Settings'), {
#             'fields': ('is_free', 'is_published')
#         }),
#         (_('Resources'), {
#             'fields': ('resources', 'attachments')
#         }),
#         (_('Timestamps'), {
#             'fields': ('created_at', 'updated_at')
#         }),
#     )


# class CourseEnrollmentAdmin(admin.ModelAdmin):
#     list_display = ['student', 'course', 'progress', 'is_active', 'enrolled_at', 'completed_at']
#     list_filter = ['is_active', 'enrolled_at', 'completed_at', 'course']
#     search_fields = ['student__username', 'student__email', 'course__title']
#     readonly_fields = ['enrolled_at', 'last_accessed']
#     ordering = ['-enrolled_at']
    
#     fieldsets = (
#         (_('Enrollment'), {
#             'fields': ('student', 'course', 'enrolled_at', 'is_active')
#         }),
#         (_('Progress'), {
#             'fields': ('progress', 'last_accessed', 'completed_at')
#         }),
#         (_('Certificate'), {
#             'fields': ('certificate_issued', 'certificate_issued_at')
#         }),
#     )


# class CourseRatingAdmin(admin.ModelAdmin):
#     list_display = ['student', 'course', 'rating', 'created_at']
#     list_filter = ['rating', 'created_at', 'course']
#     search_fields = ['student__username', 'course__title', 'review']
#     readonly_fields = ['created_at', 'updated_at']
#     ordering = ['-created_at']


# class LessonProgressAdmin(admin.ModelAdmin):
#     list_display = ['student', 'lesson', 'is_completed', 'watch_time', 'last_accessed']
#     list_filter = ['is_completed', 'last_accessed', 'lesson__course']
#     search_fields = ['student__username', 'lesson__title']
#     readonly_fields = ['last_accessed']
#     ordering = ['-last_accessed']


# class CourseCertificateAdmin(admin.ModelAdmin):
#     list_display = ['student', 'course', 'certificate_number', 'issued_at']
#     list_filter = ['issued_at', 'course']
#     search_fields = ['student__username', 'course__title', 'certificate_number']
#     readonly_fields = ['issued_at', 'certificate_number']
#     ordering = ['-issued_at']


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Course, CourseAdmin)
# admin.site.register(Lesson, LessonAdmin)
# admin.site.register(CourseEnrollment, CourseEnrollmentAdmin)
# admin.site.register(CourseRating, CourseRatingAdmin)
# admin.site.register(LessonProgress, LessonProgressAdmin)
# admin.site.register(CourseCertificate, CourseCertificateAdmin)

# admin.py

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Course, Lesson, CourseEnrollment, CourseRating, LessonProgress, CourseCertificate

# Inline for lessons inside courses
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ['title', 'order', 'duration', 'is_free', 'is_published']


# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'instructor', 'category', 'level', 'is_published', 
        'is_featured', 'enrolled_students', 'rating', 'created_at'
    ]
    list_filter = ['is_published', 'is_featured', 'level', 'category', 'instructor', 'created_at']
    search_fields = ['title', 'description', 'instructor__username', 'instructor__email']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['enrolled_students', 'rating', 'total_ratings', 'created_at', 'updated_at']
    ordering = ['-created_at']
    inlines = [LessonInline]

    fieldsets = (
        (_('Basic Information'), {
            'fields': ('title', 'slug', 'description', 'short_description', 'instructor', 'category', 'level')
        }),
        (_('Content'), {
            'fields': ('thumbnail', 'preview_video', 'duration', 'total_lessons')
        }),
        (_('Settings'), {
            'fields': ('is_free', 'price', 'is_published', 'is_featured')
        }),
        (_('SEO'), {
            'fields': ('meta_title', 'meta_description', 'keywords')
        }),
        (_('Statistics'), {
            'fields': ('enrolled_students', 'rating', 'total_ratings')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at', 'published_at')
        }),
    )


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'duration', 'is_free', 'is_published', 'created_at']
    list_filter = ['is_published', 'is_free', 'course', 'created_at']
    search_fields = ['title', 'course__title']
    ordering = ['course', 'order']

    fieldsets = (
        (_('Basic Information'), {
            'fields': ('title', 'course', 'order')
        }),
        (_('Content'), {
            'fields': ('content', 'video_url', 'duration')
        }),
        (_('Settings'), {
            'fields': ('is_free', 'is_published')
        }),
        (_('Resources'), {
            'fields': ('resources', 'attachments')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at')
        }),
    )


# Course Enrollment Admin
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'progress', 'is_active', 'enrolled_at', 'completed_at']
    list_filter = ['is_active', 'enrolled_at', 'completed_at', 'course']
    search_fields = ['student__username', 'student__email', 'course__title']
    readonly_fields = ['enrolled_at', 'last_accessed']
    ordering = ['-enrolled_at']

    fieldsets = (
        (_('Enrollment'), {
            'fields': ('student', 'course', 'enrolled_at', 'is_active')
        }),
        (_('Progress'), {
            'fields': ('progress', 'last_accessed', 'completed_at')
        }),
        (_('Certificate'), {
            'fields': ('certificate_issued', 'certificate_issued_at')
        }),
    )


# Course Rating Admin
class CourseRatingAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'course']
    search_fields = ['student__username', 'course__title', 'review']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']


# Lesson Progress Admin
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ['student', 'lesson', 'is_completed', 'watch_time', 'last_accessed']
    list_filter = ['is_completed', 'last_accessed', 'lesson__course']
    search_fields = ['student__username', 'lesson__title']
    readonly_fields = ['last_accessed']
    ordering = ['-last_accessed']


# Course Certificate Admin
class CourseCertificateAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'certificate_number', 'issued_at']
    list_filter = ['issued_at', 'course']
    search_fields = ['student__username', 'course__title', 'certificate_number']
    readonly_fields = ['issued_at', 'certificate_number']
    ordering = ['-issued_at']


# Register models to admin panel
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(CourseEnrollment, CourseEnrollmentAdmin)
admin.site.register(CourseRating, CourseRatingAdmin)
admin.site.register(LessonProgress, LessonProgressAdmin)
admin.site.register(CourseCertificate, CourseCertificateAdmin)
