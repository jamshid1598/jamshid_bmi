from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE


from .models import (
    Resume,
    Education,
    Experience,
    Portfolio,
    Image,
)

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display       = ('user', 'career',)
    list_display_links = ('user', 'career',)
    search_fields      = ('user', 'career',)
    ordering           = ('user', 'career',)

    fieldsets = (
        ('Resume', {
            "fields": (
                'user', 'career', 'image', 'about_me', 'bg_image',
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE}
    }

admin.site.register(Resume, ResumeAdmin)


class EducationAdmin(admin.ModelAdmin):
    # ('student', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', 'learned_skill' )
    list_display       = ('user', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', )
    list_display_links = ('user', 'start_at', 'end_at', )
    search_fields      = ('user', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', )
    ordering           = ('user', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', )

    fieldsets = (
        ('Education', {
            "fields": (
                'user', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', 'learned_skill'
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE}
    }

admin.site.register(Education, EducationAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display       = ('user', 'company', 'occpation', 'start_at', 'end_at', 'address', 'phone_number')
    list_display_links = ('user', 'company', 'occpation',  'start_at', 'end_at', 'address', 'phone_number')
    search_fields      = ('user', 'company', 'occpation', 'start_at', 'end_at', 'address', 'phone_number')
    ordering           = ('user', 'company', 'occpation', 'start_at', 'end_at', 'address', 'phone_number')

    fieldsets = (
        ('Experience', {
            "fields": (
                'user', 'company', 'occpation', 'qualification', 'start_at', 'end_at', 'link', 'address', 'phone_number'
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE}
    }

admin.site.register(Experience, ExperienceAdmin)


class ImageTabularInline(admin.TabularInline):
    model   = Image
    max_num = 10

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, ]

    list_display       = ('user', 'name',)
    list_display_links = ('user', 'name',)
    search_fields      = ('user', 'name',)
    ordering           = ('user', 'name',)

    fieldsets = (
        ('Portfolio', {
            "fields": (
                'user', 'name', 'image', 'link', 'short_desc', 'description',
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE}
    }

admin.site.register(Portfolio, PortfolioAdmin)




