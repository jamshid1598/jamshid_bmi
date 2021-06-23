from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE


from .models import (
    Resume,
    Education,
    Experience,
    Portfolio,
    PortfolioDetail,
    Image,
)


# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list_display       = ('student', 'career',)
    list_display_links = ('student', 'career',)
    search_fields      = ('student', 'career',)
    ordering           = ('student', 'career',)

    fieldsets = (
        ('Resume', {
            "fields": (
                'student', 'career', 'image', 'about_me', 'bg_image',
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE}
    }

admin.site.register(Resume, ResumeAdmin)


class EducationAdmin(admin.ModelAdmin):
    # ('student', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', 'learned_skill' )
    list_display       = ('student', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', )
    list_display_links = ('student', 'start_at', 'end_at', )
    search_fields      = ('student', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', )
    ordering           = ('student', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', )

    fieldsets = (
        ('Education', {
            "fields": (
                'student', 'start_at', 'end_at', 'otm_or_place_of_education', 'faculty_or_subject', 'learned_skill'
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE}
    }

admin.site.register(Education, EducationAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display       = ('student', 'company', 'occpation', 'start_at', 'end_at', 'address', 'phone_number')
    list_display_links = ('student', 'company', 'occpation',  'start_at', 'end_at', 'address', 'phone_number')
    search_fields      = ('student', 'company', 'occpation', 'start_at', 'end_at', 'address', 'phone_number')
    ordering           = ('student', 'company', 'occpation', 'start_at', 'end_at', 'address', 'phone_number')

    fieldsets = (
        ('Experience', {
            "fields": (
                'student', 'company', 'occpation', 'qualification', 'start_at', 'end_at', 'link', 'address', 'phone_number'
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE}
    }

admin.site.register(Experience, ExperienceAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display       = ('student', 'name',)
    list_display_links = ('student', 'name',)
    search_fields      = ('student', 'name',)
    ordering           = ('student', 'name',)

    fieldsets = (
        ('Portfolio', {
            "fields": (
                'student', 'name', 'image', 'link', 'short_desc',
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE}
    }

admin.site.register(Portfolio, PortfolioAdmin)


class ImageTabularInline(admin.TabularInline):
    model   = Image
    max_num = 10

class PortfolioDetailAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, ]

    list_display       = ('portfolio', )
    list_display_links = ('portfolio', )
    search_fields      = ('portfolio', )
    ordering           = ('portfolio', )

    fieldsets = (
        ('Portfolio Detail', {
            "fields": (
                'portfolio', 'description',                
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE}
    }

admin.site.register(PortfolioDetail, PortfolioDetailAdmin)
