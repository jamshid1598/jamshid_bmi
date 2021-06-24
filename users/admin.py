from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from tinymce.widgets import TinyMCE
from django.db import models


from .models import Student


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'phone_number', 'full_name',)
    list_filter = ('email', 'phone_number', 'full_name', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('-start_date',)
    list_display = ('email', 'phone_number', 'full_name', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ('User Infor', {'fields': ('email', 'phone_number', 'full_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'full_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }


admin.site.register(NewUser, UserAdminConfig)


class StudentAdmin(admin.ModelAdmin):
    list_display       = ('id', 'name_group', 'faculty', 'level', 'group')
    list_display_links = ('id', 'name_group',)
    list_editable      = ( 'faculty', 'level', 'group',)
    ordering           = ('faculty', 'level', 'group')
    search_fields      = ('faculty', 'level', 'group')

    def name_group(self, obj):
        if obj.group:
            return obj.student.full_name+" > "+obj.group
        else:
            return obj.student

    fieldsets = (
        (
            'Teacher', {
                'fields':
                ('student', 'image', 'faculty', 'level', 'group'),
            }
        ),
        
    )

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }

admin.site.register(Student, StudentAdmin)