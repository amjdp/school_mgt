from django.shortcuts import render, redirect
from school_admin. models import AdminLogin,Teacher
from teacher. models import Student

# Create your views here.
def home(request):
    return render(request,'common/home.html')

def a_login(request):
    if request.method == 'POST':
        a_username = request.POST['admin_username']
        a_password = request.POST['admin_password']

        try:
            a_login = AdminLogin.objects.get(admin_id = a_username, admin_pwd = a_password)   
            return redirect('school_admin:hom')    
        except:
            msg = 'incorrect user name and password' 
            return render(request,'common/a_login.html',{'invalid_data':msg})  

    return render(request,'common/a_login.html')

def s_login(request):
    if request.method == 'POST':
        s_username = request.POST['s_username']
        s_password = request.POST['s_password']

        try:
            s_login = Student.objects.get(student_email = s_username, student_password = s_password)  
            request.session['student_id'] = s_login.id  
            return redirect('student:hom')    
        except:
            msg = 'incorrect user name and password' 
            return render(request,'common/s_login.html',{'invalid_data':msg}) 
    return render(request,'common/s_login.html')

def t_login(request):
    if request.method == 'POST':
        t_username = request.POST['t_username']
        t_password = request.POST['t_password']

        try:
            t_login = Teacher.objects.get(teacher_email = t_username, teacher_password = t_password)   
            request.session['teacher_id'] = t_login.id 
            return redirect('teacher:hom')    
        except:
            msg = 'incorrect user name and password' 
            return render(request,'common/t_login.html',{'invalid_data':msg})  

    return render(request,'common/t_login.html')