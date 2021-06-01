from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

class Grade(models.Model):
    type = models.CharField(max_length = 2, default= "A+")

    def __str__(self):
        return self.type

class Certificate_type(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Department(models.Model):
    department = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.department

class Faculty(models.Model):
    name = models.CharField(max_length = 30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length =400)
    
    def __str__(self):
        return self.name
    

class Student(models.Model):
    full_name = models.CharField(max_length = 50)
    year_of_graduation = IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    certificate = models.ForeignKey(Certificate_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    
    
    


