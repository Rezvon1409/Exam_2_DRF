from rest_framework import serializers
from .models import Company, Vacancy, Apply


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__" 
        read_only_fields = ["owner"] 


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)  
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source="company", write_only=True)

    class Meta:
        model = Vacancy
        fields = ("id","title","description","salary","city","experience","deadline","created_at","is_active","company","company_id","user",)
        read_only_fields = ["user"]

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ("id","name","phone","cover_letter","status","created_at","vacancy_id","user",)
        read_only_fields = ["user"] 