from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, UserProfile, UserActivity


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('email', 'username', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active', 'email_verified', 'created_at')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': ('username', 'first_name', 'last_name', 'bio', 'avatar', 
                      'date_of_birth', 'phone_number', 'user_type')
        }),
        (_('Social Media'), {
            'fields': ('website', 'linkedin', 'github', 'twitter')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Email Verification'), {'fields': ('email_verified', 'email_verification_token')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'user_type'),
        }),
    )


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill_level', 'total_courses_enrolled', 'total_courses_completed', 'completion_rate')
    list_filter = ('skill_level', 'created_at')
    search_fields = ('user__email', 'user__username')
    readonly_fields = ('total_courses_enrolled', 'total_courses_completed', 'total_learning_hours', 'certificates_earned', 'badges_earned')
    
    fieldsets = (
        (_('User Information'), {
            'fields': ('user', 'skill_level', 'learning_goals', 'interests', 'preferred_languages')
        }),
        (_('Progress Statistics'), {
            'fields': ('total_courses_enrolled', 'total_courses_completed', 'total_learning_hours', 'certificates_earned', 'badges_earned')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at')
        }),
    )


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'description', 'timestamp')
    list_filter = ('activity_type', 'timestamp')
    search_fields = ('user__email', 'user__username', 'description')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)
    
    fieldsets = (
        (_('Activity Information'), {
            'fields': ('user', 'activity_type', 'description')
        }),
        (_('Related Object'), {
            'fields': ('related_object_id', 'related_object_type')
        }),
        (_('Timestamp'), {
            'fields': ('timestamp',)
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserActivity, UserActivityAdmin)
