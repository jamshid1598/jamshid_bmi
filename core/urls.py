from django.urls import path

from .views import (
    HomeView, 
    PortfolioView,
    PortfolioDetailView,
    GuideView,


    FeedbackView,
)

app_name='portfolio'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio-detail/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('guide/', GuideView.as_view(), name='guide'),
    path('contact/', FeedbackView.as_view(), name='contact'),
]