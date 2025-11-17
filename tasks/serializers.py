from rest_framework import serializers
from .models import Category, Vacancy, Application
from accounts.models import CustomUser

# Serializer барои категорияҳо
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']  # Намоиши ID, ном ва тавсиф

# Serializer барои вакансияҳо
class VacancySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Намоиши категория бо маълумоти пурра
    employer = serializers.StringRelatedField(read_only=True)  # Намоиши корфармо бо номи ӯ
    assigned_worker = serializers.StringRelatedField(read_only=True)  # Намоиши коргари таъиншуда

    class Meta:
        model = Vacancy
        fields = ('id','title','description','salary','category','employer','assigned_worker','is_filled','created_at')

# Serializer барои эҷод ва таҳрири вакансия
class VacancyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('title','description','salary','category')

# Serializer барои дархостҳо
class ApplicationSerializer(serializers.ModelSerializer):
    worker = serializers.StringRelatedField(read_only=True)  # Намоиши коргар
    vacancy = serializers.StringRelatedField(read_only=True)  # Намоиши вакансия

    class Meta:
        model = Application
        fields = ['id', 'worker', 'vacancy', 'applied_at', 'is_accepted']


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['vacancy']  # Коргар автомат аз user request гирифта мешавад
