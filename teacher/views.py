from django.shortcuts import render,redirect
from school_admin.models import Teacher
from teacher.models import Student  
from .decorators import auth_teacher

# Create your views here.

@auth_teacher
def t_home(request):
    # if 'teacher_id' in request.session:
        teacher = Teacher.objects.get(id = request.session['teacher_id'])
        return render(request,'teacher/t_home.html',{'teacher_data': teacher})
    # else: 
    #     return redirect('t_login')
@auth_teacher
def prof(request):
    return render(request,'teacher/profile.html')

@auth_teacher
def view_st(request):
    students = Student.objects.filter(teacher = request.session['teacher_id'])
    return render(request,'teacher/view_student.html',{'student_list':students})

@auth_teacher
def add_st(request):
    msg = ""
    if request.method == 'POST':
        s_name = request.POST['s_name']
        s_email = request.POST['s_email']
        s_dob = request.POST['s_dob']
        s_phone_number = request.POST['s_ph_no']
        s_place = request.POST['s_place']
        parent_name = request.POST['p_name']
        s_photo = request.FILES['s_photo']  
        s_password = request.POST['s_password'] 

       #exist() not in get - only in filter -  result will be boolean
        email_exist = Student.objects.filter(student_email = s_email).exists()  

        if not email_exist:
            student = Student(
                student_name = s_name, 
                student_email = s_email, 
                student_dob = s_dob,
                student_phone_number = s_phone_number, 
                student_place = s_place, 
                s_parent_name = parent_name,
                student_profile_picture = s_photo, 
                student_password = s_password, 
                teacher_id = request.session['teacher_id'])
            student.save()
            msg = "Student added successfully"
        else:
            msg = "Student already added"

    return render(request,'teacher/add_student.html',{'status':msg})

@auth_teacher
def chg_pwd(request):
    msg = ""
    if request.method == 'POST':
        t_old_pwd = request.POST['old_pwd']
        t_new_pwd = request.POST['new_pwd']
        t_confirm_pwd = request.POST['confirm_pwd']

        teacher = Teacher.objects.get(id = request.session['teacher_id'])
        # teacher.teacher_password = '123'
        # teacher.save()

        if teacher.teacher_password == t_old_pwd:
            if t_new_pwd == t_confirm_pwd:
                teacher.teacher_password = t_new_pwd
                teacher.save()
                msg = "Password changed successfully"
            else:
                msg = "password does not match" 
        else:
            msg = "incorrect password"

    return render(request,'teacher/change_password.html',{'status':msg})

def logout(request):
    del request.session['teacher_id']
    request.session.flush()
    return redirect('hom')