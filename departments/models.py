from django.db import models

class Departments(models.Model):
    emp_name = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    def __str__(self):
        return self.emp_name