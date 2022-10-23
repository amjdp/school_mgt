from django.shortcuts import render
from .models import Student

# Create your views here.
def t_home(request):
    return render(request,'teacher/t_home.html')

def prof(request):
    return render(request,'teacher/profile.html')

def view_st(request):
    return render(request,'teacher/view_student.html')

def add_st(request):
    if request.method == 'POST':
        s_name = request.POST['s_name']
        s_email = request.POST['s_email']
        s_dob = request.POST['s_dob']
        s_phone_number = request.POST['s_ph_no']
        s_place = request.POST['s_place']
        parent_name = request.POST['p_name']
        s_photo = request.FILES['s_photo']  
        s_password = request.POST['s_password']      
        student = Student(student_name = s_name, student_email = s_email, student_dob = s_dob, 
        student_phone_number = s_phone_number, student_place = s_place, s_parent_name = parent_name, 
        student_profile_picture = s_photo, student_password = s_password)        
        student.save()
    return render(request,'teacher/add_student.html')

def chg_pwd(request):
    return render(request,'teacher/change_password.html')