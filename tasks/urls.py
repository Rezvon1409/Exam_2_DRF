from django.urls import path
from .views import *

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),
    path('applies/', ApplyListAPIView.as_view()),
    path('applies/<int:pk>/', ApplyDetailAPIView.as_view()),
]
