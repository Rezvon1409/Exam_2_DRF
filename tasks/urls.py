from django.urls import path
from .views import CategoryListAPIView,VacancyListAPIView,VacancyCreateAPIView,VacancyDetailAPIView,ApplicationListAPIView,ApplicationCreateAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('vacancies/', VacancyListAPIView.as_view(), name='vacancy-list'),
    path('vacancies/create/', VacancyCreateAPIView.as_view(), name='vacancy-create'),
    path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view(), name='vacancy-detail'),
    path('applications/', ApplicationListAPIView.as_view(), name='application-list'),
    path('applications/create/', ApplicationCreateAPIView.as_view(), name='application-create'),
]
