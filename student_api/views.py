from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student1
from . serializer import StudentSerializer 
from django.http import JsonResponse

@api_view(['GET']) 
def load_student(request):
    students = Student1.objects.all()
    serialized_data = StudentSerializer(students, many = True)
    return JsonResponse(serialized_data.data, safe = False)
    
@api_view(['POST'])
def add_student(request):
    serialized_data = StudentSerializer(data = request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'message':'data inserted successfully'})
    else:
        print('Invalid data')
        return JsonResponse({'message':'error'})

@api_view(['DELETE'])
def del_student(request,s_id):
    student = Student1.objects.get(id = s_id)
    student.delete()
    return JsonResponse({'message':'deleted Successfully'})

@api_view(['PUT'])
def update_student(request,s_id):
    student = Student1.objects.get(id = s_id)
    serialized_data = StudentSerializer(student,data = request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'message':'data updated successfully'})
    else:
        return JsonResponse({'message':'error'})

@api_view(['GET'])
def index(request):
    message = 'Congratulations... you have created an API'
    return Response(message)

@api_view(['GET'])
def number(request):
    message = 10
    return Response(message)

def signup(request):    
    return render(request,'student_api/signup.html')

def validation(request):    
    return render(request,'student_api/from_validation.html')