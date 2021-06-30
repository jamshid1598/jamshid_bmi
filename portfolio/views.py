from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse, BadHeaderError
from django.core import serializers
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from django.template import defaultfilters
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Case, Value, When, Q, F
import json

from django.contrib.auth import get_user_model
User = get_user_model()

from users.models import Student

from .forms import(
	ResumeForm,
	PortfolioForm,
	ContactForm,
)
from .models import (
	Resume,
	Education,
	Experience,
	Portfolio,
	Image,
)

# Create your views here.

class HomeView(View):
	template_name='portfolio/index.html'
	def get(self, request, *args, **kwargs):
		context={}
		return render(request, self.template_name, context)

class PortfolioView(View):
	template_name='portfolio/portfolio.html'
	def get(self, request, *args, **kwargs):
		object_list = Portfolio.objects.all()
		user=None
		if object_list:
			for obj in object_list:
				user = obj.user
		else:
			user="new"
		context={"object_list": object_list, 'user':user}
		return render(request, self.template_name, context)


class PortfolioDetailView(View):
	template_name='portfolio/portfolio-detail.html'
	def get(self, request, pk, *args, **kwargs):
		obj = Portfolio.objects.get(pk=pk)
		print(obj)
		context={'object':obj}
		return render(request, self.template_name, context)


class ContactView(View):
	template_name='portfolio/contact.html'
	def get(self, request, *args, **kwargs):
		form=ContactForm()
		context={'form':form}
		return render(request, self.template_name, context)
	
	def post(self, request, *args, **kwargs):
		form=ContactForm()
		context={'form':form}
		return render(request, self.template_name, context)


@login_required
def portfolio_form(request):
	if request.method == 'POST':
		form = PortfolioForm(request.POST, request.FILES)
		if form.is_valid():
			print("hello")
			print(form.cleaned_data.get('user'))
			print(form.cleaned_data.get('name'))
			print(form.cleaned_data.get('image'))
			print(form.cleaned_data.get('link'))
			print(form.cleaned_data.get('short_desc'))
			print(form.cleaned_data.get('description'))

			user = User.objects.get(pk=form.cleaned_data.get('user'))
			Portfolio.objects.create(
				user        = user,
				name        = form.cleaned_data.get('name'),
				image       = form.cleaned_data.get('image'),
				link        = form.cleaned_data.get('link'),
				short_desc  = form.cleaned_data.get('short_desc'),
				description = form.cleaned_data.get('description'),
				file        = form.cleaned_data.get('file'),
				document    = form.cleaned_data.get('document'),
			)
		else:
			for msg in form.errors:
				messages.error(request, f"{msg}: {form.errors[msg]}")

	return redirect('portfolio_2:portfolio')


def student_info_form(request):
	if request.method == 'POST':
		form = ResumeForm(request.POST, request.FILES)
		if form.is_valid():
			user = User.objects.get(pk=form.cleaned_data.get('student'))
			student = Student.objects.get(student=user)
			Resume.objects.create(
				student = student,
				image = form.cleaned_data.get('image'),
				bg_image = form.cleaned_data.get('bg_image'),
				career = form.cleaned_data.get('career'),
				about_me = form.cleaned_data.get('about_me'),
			)
		else:
			for msg in form.errors:
				messages.error(request, f"{msg}: {form.errors[msg]}")

	return redirect('portfolio_2:home')