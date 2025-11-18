from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Vacancy, Apply
from .serializers import CompanySerializer, VacancySerializer, ApplySerializer


class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailAPIView(APIView):
    def get(self, request, pk):
        company = Company.objects.filter(pk=pk).first()
        if not company:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = Company.objects.filter(pk=pk).first()
        if not company:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = Company.objects.filter(pk=pk).first()
        if not company:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.filter(is_active=True)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacancyDetailAPIView(APIView):
    def get(self, request, pk):
        vacancy = Vacancy.objects.filter(pk=pk).first()
        if not vacancy:
            return Response({"error": "Vacancy not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, pk):
        vacancy = Vacancy.objects.filter(pk=pk).first()
        if not vacancy:
            return Response({"error": "Vacancy not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vacancy = Vacancy.objects.filter(pk=pk).first()
        if not vacancy:
            return Response({"error": "Vacancy not found"}, status=status.HTTP_404_NOT_FOUND)
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ApplyListAPIView(APIView):
    def get(self, request):
        applies = Apply.objects.all()
        serializer = ApplySerializer(applies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplyDetailAPIView(APIView):
    def get(self, request, pk):
        apply = Apply.objects.filter(pk=pk).first()
        if not apply:
            return Response({"error": "Application not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ApplySerializer(apply)
        return Response(serializer.data)

    def put(self, request, pk):
        apply = Apply.objects.filter(pk=pk).first()
        if not apply:
            return Response({"error": "Application not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ApplySerializer(apply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        apply = Apply.objects.filter(pk=pk).first()
        if not apply:
            return Response({"error": "Application not found"}, status=status.HTTP_404_NOT_FOUND)
        apply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
