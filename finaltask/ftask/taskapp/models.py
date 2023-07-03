from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FormEntry(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    purpose = models.CharField(max_length=20)
    materials = models.CharField(max_length=100)

    def __str__(self):
        return self.name
