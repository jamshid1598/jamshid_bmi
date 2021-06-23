from django import forms
from phonenumber_field.formfields import PhoneNumberField

class FeedbackForm(forms.Form):
	full_name    = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'type':"text", 'class':"form-control", 'id':"exampleInputFullName", 'placeholder': 'John Doe'}))
	phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"exampleInputPhoneNumber", 'placeholder': "+998 -- --- -- --"}))
	email        = forms.EmailField(widget=forms.EmailInput(attrs={'type':"email", 'class':"form-control", 'id':"exampleInputEmail",  'placeholder': "example@gmail.com"}))
	text         = forms.CharField(widget=forms.Textarea(attrs={'type':"text", 'class':"form-control", 'id':"exampleInputFeedback",  "placeholder" : "write here your question/feedback"}))