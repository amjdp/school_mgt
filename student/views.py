from django.shortcuts import render

from teacher.models import Student

# Create your views here.
def s_home(request):
    return render(request,'student/s_home.html')

def prof(request):
    return render(request,'student/profile.html')

def chg_pwd(request):
    msg = ""
    if request.method == 'POST':
        s_old_pwd = request.POST['old_pwd']
        s_new_pwd = request.POST['new_pwd']
        s_confirm_pwd = request.POST['confirm_pwd']

        student = Student.objects.get(id = request.session['student_id'])
        if student.student_password == s_old_pwd:
            if s_new_pwd == s_confirm_pwd:
                Student.objects.filter(id = request.session['student_id']).update(student_password = s_new_pwd)
                # student.student_password = s_new_pwd
                # student.save()
                msg = "Password changed successfully"
            else:
                msg = "Password does not match"
        else:
            msg = "incorrect password"

    return render(request,'student/change_password.html',{'status':msg})

