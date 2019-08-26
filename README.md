# DJango RestFramework API

What is DJango
------
> Django is a free and open source web application framework written in Python. It offers a big collection of modules that make development easier. They are grouped together, and allow you to create applications or websites from an existing source, instead of from scratch.

> It is "a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source".

What is DJango RestFramework
------
> Django REST framework is a powerful and flexible toolkit for building Web APIs.

Steps for creating django rest API
------
> In this example, we are implementing sample REST API for employee + department. We can fetch/ add/ modify/ delete employee details including employee name and department name using DJango REST API framework.

##### Install DJango RestFramework / prerequisites
> install django (if django is not installed on your machine)
`pip install django`
> use this command to install djangorestframework
`pip install djangorestframework`
> **OR**
> use this command for user specific installation 
`pip install djangorestframework --user`

##### Project setupProject setupProject setupProject setup

> Create new django project called **employee_api**

```python
mkdir django_restapi_demo
cd django_restapi_demo
django-admin create employee_api
```
 > Create django app 

```python 
django-admin startapp departments
```

##### Modify your django application settings.py
> Add 'rest_framework' and 'departments' app to your INSTALLED_APPS in settings.py.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
	'departments',
]
```
##### Implement DJango RestFramework

> Define URLS on employee/urls.py

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('departments.urls')),
]
```
> Now sync your database for the first time & Create superuser for the first time

```python
python manage.py migrate
python manage.py createsuperuser```

> Create a model for employee_api on departments/models.py

```python
from django.db import models
class Departments(models.Model):
    emp_name = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    def __str__(self):
        return self.emp_name
```
> sync DB with changes

```python
python manage.py makemigrations
python manage.py migrate
```

> Add your **departments** model into admin console. We can navigate and check the entries on db http://localhost:8000/admin

```python
from django.contrib import admin
from .models import Departments
admin.site.register(Departments)
```
 > Create Serializers on departments/serializers.py
 
 ```python
from rest_framework import serializers
from .models import Departments

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'emp_name', 'dept_name','url')
```
 > Update views as per the serializers on departments/views.py
 
 ```python
from django.shortcuts import render
from rest_framework import viewsets
from .models import Departments
from .serializers import DepartmentSerializer

class DepartmentView(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
```
 > Now lets define the API URLs using automatic URL routing. on departments/urls.py
 
 ```python
from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('department', views.DepartmentView)

urlpatterns = [
   path('', include(router.urls))
]
```
 > Test API on browser/ postman/ any api client
 
 ```python
 python manage.py runserver
 ```

`Note: Above django project prepared and tested on django==2.2.3 and djangorestframework==3.10.2`
