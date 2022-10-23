from django.shortcuts import render
from school_admin. models import Teacher

# Create your views here.
def a_home(request):
    return render(request,'school_admin/a_home.html')

def add_tr(request):
    if request.method == 'POST':
        t_name = request.POST['t_name']
        t_email = request.POST['t_email']
        t_address = request.POST['t_address']
        t_qualification = request.POST['t_qualification']
        t_dob = request.POST['t_dob']
        t_gender = request.POST['t_gender']
        t_exp = request.POST['t_exp']
        t_photo = request.FILES['t_photo']  
        t_password = request.POST['t_password']      
        teacher = Teacher(teacher_name = t_name, teacher_email = t_email, teacher_address = t_address, 
        qualification = t_qualification, teacher_dob = t_dob, teacher_gender = t_gender, exp = t_exp, 
        teacher_profile_picture = t_photo, teacher_password = t_password)        
        teacher.save()
    return render(request,'school_admin/add_teacher.html')

def view_st(request):
    return render(request,'school_admin/view_student.html')

def view_tr(request):
    return render(request,'school_admin/view_teachers.html')

def chg_pwd(request):
    return render(request,'school_admin/change_password.html')