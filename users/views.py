from django.urls import  reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, render

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .forms import NewUserForm, UserLoginForm


class NewUserCreationView(SuccessMessageMixin, CreateView):
	template_name = 'registration/signup.html'
	form_class = NewUserForm
	success_url = reverse_lazy('login')
	success_message = "New account for %(full_name)s was created successfully, now you can login"
   
	def get_success_message(self, cleaned_data):
		return self.success_message % dict(
			cleaned_data,
			full_name=self.object.full_name,
		)


def login_view(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			email    = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			print(email, password)
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "Welcome come back {}".format(user.full_name))
				return redirect("portfolio:home")
			else: 
				messages.error(request, "invaled username or password")
		else: 
			messages.error(request, "invaled username or password")

	form = UserLoginForm()
	return render(
			request=request,
			template_name="registration/login.html",
			context={
				'form' : form
			}
		)


@login_required
def logout_view(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("portfolio:home")


