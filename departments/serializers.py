from rest_framework import serializers

from .models import Departments
class DepartmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'emp_name', 'dept_name', 'url')