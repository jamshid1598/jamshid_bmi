from django.urls import path

from .views import (
    HomeView, 
    PortfolioView,
    ExampleView,
    ExampleDetailView,
    GuideView,


    FeedbackView,
)

app_name='portfolio'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('example/', ExampleView.as_view(), name='example'),
    path('example-detail/', ExampleDetailView.as_view(), name='example-detail'),
    path('guide/', GuideView.as_view(), name='guide'),
    path('contact/', FeedbackView.as_view(), name='contact'),
]