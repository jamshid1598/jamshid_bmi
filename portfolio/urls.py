from django.urls import path

from .views import (
    HomeView,
    PortfolioView,
    PortfolioDetailView,
    ContactView,


    portfolio_form,
    student_info_form,
)

app_name='portfolio_2'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/detail/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('contact/', ContactView.as_view(), name='contact'),


    path('portfolio/form/', portfolio_form, name='portfolio-form'),
    path('student/form/', student_info_form, name='student-form'),
]