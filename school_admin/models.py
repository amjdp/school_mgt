from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length = 25)   # varchar(25)
    teacher_email = models.CharField(max_length = 30)
    teacher_address = models.CharField(max_length = 100)
    qualification = models.CharField(max_length = 30)
    exp = models.IntegerField()
    teacher_dob = models.CharField(max_length = 100)
    teacher_gender = models.CharField(max_length = 10)    
    teacher_profile_picture = models.ImageField(upload_to = 'teacher/')
    teacher_password = models.CharField(max_length = 20)

class AdminLogin(models.Model):
    admin_id = models.CharField(max_length = 25)   # varchar(25)
    admin_pwd = models.CharField(max_length = 30)
    