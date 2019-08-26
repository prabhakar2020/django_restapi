from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Departments
from .serializers import DepartmentsSerializer
class DepartmentView(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer