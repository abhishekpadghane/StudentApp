from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=20, blank=True, null=True)
    student_age = models.IntegerField(blank=True, null=True)
    student_address = models.TextField(blank=True, null=True)
    student_image = models.ImageField(upload_to='images/', null=True, blank=True)
