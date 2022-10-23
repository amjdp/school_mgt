from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length = 30)   # varchar(25)
    student_email = models.CharField(max_length = 30)   
    student_dob = models.CharField(max_length = 20)
    student_phone_number = models.BigIntegerField()
    student_place = models.CharField(max_length = 30)
    s_parent_name = models.CharField(max_length = 30)    
    student_profile_picture = models.ImageField(upload_to = 'student/')
    student_password = models.CharField(max_length = 20)