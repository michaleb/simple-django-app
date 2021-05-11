from django.db import models
from datetime import datetime

class School(models.Model):
    name = models.CharField(max_length =400)
    
class Faculty(models.Model):
    name = models.CharField(max_length = 30)
    faculty = models.ForeignKey(School, on_delete=models.CASCADE)
    
    
class Department(models.Model):
    department = models.CharField(max_length = 50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    

class Grade(models.Model):
    type = models.DecimalField(decimal_places = 2, max_digits = 3)

class Certificate_type(models.Model):
    name = models.CharField(max_length = 30)

class Student(models.Model):
    
    full_name = models.CharField(max_length = 50)
    year_of_graduation = models.DateField(default =datetime.today().year)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    certificate = models.ForeignKey(Certificate_type, on_delete=models.CASCADE)

    
    
    


