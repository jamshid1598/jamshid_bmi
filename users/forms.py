from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField


User = get_user_model()

class UserLoginForm(forms.Form):
	email = forms.EmailField(
		widget=forms.EmailInput(attrs={
			'type':'text', 'id':"id_email", 'name':"email", 'style':"font-size: 18px;", "class":"form-control",  'aria-describedby':"emailHelp", 'placeholder':"Enter email",
			}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'id':"id_password", 'name':"password", 'type':"password", 'style':"font-size: 18px;", 'class':"form-control", 'placeholder':"Password",
			}))
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		print(email, password)
		return email
		

class NewUserForm(UserCreationForm):
	email = forms.EmailField(
		required=True,
		widget=forms.EmailInput(attrs={'type':"email", 'class':"form-control", 'id':"exampleInputEmail1", 'placeholder':"e.x example@gmail.com"}), #class="form__input" id="email" name="email" type="email" placeholder="Elektron pochta"
	)
	full_name = forms.CharField(
		required=True,
		widget=forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"exampleInputFullName1", 'placeholder':"e.x John Doe"}), #class="form__input" id="Name" name="Name" type="text" placeholder="IFSH"
	)
	phone_number = PhoneNumberField(
		widget=forms.TextInput(
			attrs={'type':"text", 'class':"form-control", 'id':"exampleInputPhoneNumber", 'placeholder':"e.x +998 -- --- -- --"}
		)
	)
	password1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={'type':"password", 'name':'password1', 'class':"form-control", 'id':"exampleInputPassword1", 'placeholder':"e.x *********"}), #class="form__input" id="password" name="password" type="password" placeholder="Parol"
		help_text=password_validation,
	)
	
	password2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={'type':"password", 'name':'password2', 'class':"form-control", 'id':"exampleInputPassword1", 'placeholder':"e.x *********",}), #class="form__input" id="password1" name="password" type="password" placeholder="Parol tasdiqlash"
		help_text=password_validation,
	)

	class Meta:
		model=User
		fields = ("email", "full_name", "phone_number", "password1", "password2")
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		queryset=User.objects.filter(email=email)
		if queryset.exists():
			raise forms.ValidationError(_('Ushbu elektron pochta allaqachon mavjud'))
		return email
	
	def clean_phone_number(self):
		phone_number=self.cleaned_data.get('phone_number')
		queryset=User.objects.filter(phone_number=phone_number)
		if queryset.exists():
			raise forms.ValidationError(_("Bu raqam allaqachon ro'yhatdan o'tkan"))
		return phone_number

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
	   
		if commit:
			user.save()
		return user

