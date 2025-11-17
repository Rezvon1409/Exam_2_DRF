from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Category, Vacancy, Application
from .serializers import CategorySerializer,VacancySerializer,VacancyCreateSerializer,ApplicationSerializer,ApplicationCreateSerializer


class CategoryListAPIView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class VacancyListAPIView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VacancyCreateAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = VacancyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacancyDetailAPIView(APIView):
 
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            return None

    def get(self, request, pk):
        vacancy = self.get_object(pk)
        if not vacancy:
            return Response({"detail": "Vacancy not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        vacancy = self.get_object(pk)
        if not vacancy:
            return Response({"detail": "Vacancy not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = VacancyCreateSerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vacancy = self.get_object(pk)
        if not vacancy:
            return Response({"detail": "Vacancy not found"}, status=status.HTTP_404_NOT_FOUND)
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ApplicationListAPIView(APIView):
 
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        applications = Application.objects.filter(worker=request.user)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ApplicationCreateAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ApplicationCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(worker=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
