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
User=get_user_model()

from .forms import FeedbackForm
from portfolio.models import (
	Resume,
    Education,
    Experience,
    Portfolio,
    Image,
)
# Create your views here.

class HomeView(View):
	template_name='index.html'
	def get(self, request, *args, **kwargs):
		context={}
		return render(request, self.template_name, context)


class PortfolioView(View):
	template_name='portfolio.html'
	def get(self, request, *args, **kwargs):
		object_list = Portfolio.objects.all()
		context={"object_list":object_list}
		return render(request, self.template_name, context)

class PortfolioDetailView(View):
	template_name='portfolio-detail.html'
	def get(self, request, pk=None, *args, **kwargs):
		obj = Portfolio.objects.get(pk=pk)
		context={'object': obj}
		return render(request, self.template_name, context)


class GuideView(View):
	template_name='guide.html'
	def get(self, request, *args, **kwargs):
		context={}
		return render(request, self.template_name, context)


class FeedbackView(View):
	template_name='contact.html'
	def get(self, request, *args, **kwargs):
		form=FeedbackForm()
		context={'form': form}
		return render(request, self.template_name, context)
	
	def post(self, request, *args, **kwargs):
		if request.method == "POST":
			form = FeedbackForm(request.POST)
			if form.is_valid():
				full_name    = form.cleaned_data['full_name']
				email        = form.cleaned_data['email']
				phone_number = form.cleaned_data['phone_number']
				text         = form.cleaned_data['text']

				try:
					subject = "New Message"
					thoughts = f"New message from {full_name}:\nTel: {phone_number}\nEmail: {email}\n\n{text}"
					sender = settings.EMAIL_HOST_USER
					recipients = ['dovurovjamshid95@gmail.com']

					send_mail(subject, thoughts, sender, recipients, fail_silently=False)

					messages.success(request, f"{full_name} your message was successfully send.")
				except BadHeaderError:
					return HttpResponse('Invalid header')
				return redirect('portfolio:contact')
			else:
				for msg in form.errors:
					messages.error(request, f"{msg}")
				return redirect('portfolio:contact')
		form = FeedbackForm()
		self.context = {'form': form}

		return render(
			request,
			self.template_name,
			self.context
		)

