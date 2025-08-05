# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['Get'])
def studentView(request):
    # students=Students.objects.all() #this brings the data of students model into students
    # student_list=list(students.values()) #converting query sets into list
    # return JsonResponse(student_list, safe=False) #safe parameter is for data is other than dictionaries
    
    if request.method =='GET':
        #Get all the data from the Student table
        Student = Students.objects.all()
        serializer = StudentSerializer(Student,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
