from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentView(request):
    students={
        'id':1,
        'name':'XYZ',
        'class': 'Computer Science'
    }
    return JsonResponse(students)
