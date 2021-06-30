from django import forms
from django.db import models
from django.forms.widgets import Textarea
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
    user    = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'id':"student_id", 'value':'', 'style':"width: 100%;", 'name':'student'}))
    image   = forms.ImageField(widget=forms.FileInput(attrs={'type':"file", 'id':"yourimage", 'style':"width: 100%;", 'name':'image'}))
    bg_image= forms.ImageField(widget=forms.FileInput(attrs={'type':"file", 'id':"bacgraundimage", 'style':"width: 100%;", 'name':'bg_image'}))
    career  = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':'career', 'name':"career"}))
    about_me= forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'id':'about_me', 'name':'about_me'}))


class EducationForm(forms.ModelForm):
    user     = forms.CharField(widget=forms.TextInput(attrs={}))
    start_at = forms.DateField(widget=forms.DateInput(attrs={}))
    end_at   = forms.CharField(widget=forms.TextInput(attrs={}))
    otm_or_place_of_education = forms.CharField(widget=forms.TextInput(attrs={}))
    faculty_or_subject        = forms.CharField(widget=forms.TextInput(attrs={}))
    learned_skill             = forms.CharField(widget=forms.TextInput(attrs={}))

    class Meta:
        model = Education
        fields='__all__'


class ExperienceForm(forms.ModelForm):
    user          = forms.CharField(widget=forms.TextInput(attrs={}))
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


class PortfolioForm(forms.Form):
    user        = forms.CharField(widget=forms.TextInput(attrs={'type':"hidden", 'id':"user", 'value':'', 'style':"width: 100%;", 'name':'user'}))
    name        = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':'name', 'name':"name"}))
    image       = forms.ImageField(widget=forms.FileInput(attrs={'type':"file", 'id':"image", 'style':"width: 100%;", 'name':'image'}))
    link        = forms.URLField(widget=forms.URLInput(attrs={'type':"text", 'class':"form-control", 'id':'link', 'name':"link"}))
    short_desc  = forms.CharField(widget=Textarea(attrs={'id':'short_desc', 'class':"form-control", 'name':'short_desc'}))
    description = forms.CharField(widget=Textarea(attrs={ 'id':'description',  'class':"form-control", 'name':"description"}))

    file       = forms.FileField(widget=forms.FileInput(attrs={'type':"file", 'id':"file", 'style':"width: 100%;", 'name':'file', },), required=False)
    document   = forms.FileField(widget=forms.FileInput(attrs={'type':"file", 'id':"document", 'style':"width: 100%;", 'name':'document'}), required=False)

    # class Meta:
    #     model = Portfolio
    #     fields='__all__'

class ContactForm(forms.Form):
	full_name    = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={ 'type':"text", 'id':"exampleInputFullName1", 'name':"exampleInputFullName1", 'class':"form-control", 'placeholder': 'Dovurov Jamshid'}))
	phone_number = PhoneNumberField(widget=forms.TextInput(
        attrs={'type':"text", 'id':"exampleInputPhoneNumber", 'class':"form-control", 'placeholder': "+998 -- --- -- --"}))
	email        = forms.EmailField(widget=forms.EmailInput(
        attrs={'type':"text", 'id':"exampleInputEmail1", 'name':"exampleInputEmail1", 'class':"form-control",  'placeholder': "example@gmail.com"}))
	text         = forms.CharField(widget=forms.Textarea(
        attrs={'class':"form-control", 'id':'exampleInputText', 'name':'exampleInputText',  "placeholder" : "Xabaringizni/savolingizni yozing"}))


"""

<!-- Creating user instance by passing requested user id -->
    <script>
        var user_id = "{{ request.user.id }}";
        document.getElementById('username').value=user_id;
    </script>
<!-- end -->

"""