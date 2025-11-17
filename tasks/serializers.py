from rest_framework import serializers
from .models import Category, Vacancy, Application
from accounts.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']  


class VacancySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True) 
    employer = serializers.StringRelatedField(read_only=True) 
    assigned_worker = serializers.StringRelatedField(read_only=True) 

    class Meta:
        model = Vacancy
        fields = ('id','title','description','salary','category','employer','assigned_worker','is_filled','created_at')


class VacancyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('title','description','salary','category')


class ApplicationSerializer(serializers.ModelSerializer):
    worker = serializers.StringRelatedField(read_only=True)  
    vacancy = serializers.StringRelatedField(read_only=True)  

    class Meta:
        model = Application
        fields = ['id', 'worker', 'vacancy', 'applied_at', 'is_accepted']


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['vacancy']  
