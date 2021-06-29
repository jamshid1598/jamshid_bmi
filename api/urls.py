from django.urls import path
from .views import (
    ListPortfolioApiView,
    DetailPortfolioApiView,
)

app_name='api_portfolio'

urlpatterns = [
    path('', ListPortfolioApiView.as_view(), name='portfolio-list-api'),
    path('detail/<int:pk_field>/', DetailPortfolioApiView.as_view(), name='portfolio-detail-api'),

]