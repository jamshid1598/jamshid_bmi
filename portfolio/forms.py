from django import forms
from django.db import models
from tinymce.widgets import TinyMCE
from phonenumber_field.formfields import PhoneNumberField

from .models import (
    Resume,
    Education,
    Experience,
    Portfolio,
    Image,
)



class ResumeForm(forms.Form):
    student = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'id':"student_id", 'value':'', 'style':"width: 100%;", 'name':'student'}))
    image   = forms.ImageField(widget=forms.FileInput(attrs={'type':"file", 'id':"yourimage", 'style':"width: 100%;", 'name':'image'}))
    bg_image= forms.ImageField(widget=forms.FileInput(attrs={'type':"file", 'id':"bacgraundimage", 'style':"width: 100%;", 'name':'bg_image'}))
    career  = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':'career', 'name':"career"}))
    about_me= forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'id':'about_me', 'name':'about_me'}))


class EducationForm(forms.ModelForm):
    student  = forms.CharField(widget=forms.TextInput(attrs={}))
    start_at = forms.DateField(widget=forms.DateInput(attrs={}))
    end_at   = forms.CharField(widget=forms.TextInput(attrs={}))
    otm_or_place_of_education = forms.CharField(widget=forms.TextInput(attrs={}))
    faculty_or_subject        = forms.CharField(widget=forms.TextInput(attrs={}))
    learned_skill             = forms.CharField(widget=forms.TextInput(attrs={}))

    class Meta:
        model = Education
        fields='__all__'


class ExperienceForm(forms.ModelForm):
    student       = forms.CharField(widget=forms.TextInput(attrs={}))
    student       = forms.CharField(widget=forms.TextInput(attrs={}))
    company       = forms.CharField(widget=forms.TextInput(attrs={}))
    occpation     = forms.CharField(widget=forms.TextInput(attrs={}))
    qualification = forms.CharField(widget=forms.Textarea(attrs={}))
    start_at      = forms.DateField(widget=forms.DateInput(attrs={}))
    end_at        = forms.DateField(widget=forms.DateInput(attrs={}))
    link          = forms.URLField(widget=forms.URLInput(attrs={}))
    address       = forms.CharField(widget=forms.TextInput(attrs={}))
    phone_number  = PhoneNumberField(widget=forms.TextInput(attrs={}))

    class Meta:
        model = Experience
        fields='__all__'


class PortfolioForm(forms.ModelForm):
    student    = forms.CharField(widget=forms.TextInput(attrs={}))
    name       = forms.CharField(widget=forms.TextInput(attrs={}))
    image      = forms.ImageField(widget=forms.FileInput(attrs={}))
    link       = forms.URLField(widget=forms.URLInput(attrs={}))
    short_desc = forms.CharField(widget=TinyMCE(attrs={}))
    description = forms.CharField(widget=TinyMCE(attrs={}))

    class Meta:
        model = Portfolio
        fields='__all__'



"""

<!-- Creating user instance by passing requested user id -->
    <script>
        var user_id = "{{ request.user.id }}";
        document.getElementById('username').value=user_id;
    </script>
<!-- end -->

"""