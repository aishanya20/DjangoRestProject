from django.urls import path ,include
from . import views
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='Employee')

urlpatterns=[
    path('students', views.studentView),
    path('students/<int:pk>/',views.studentDetailView),    #pk= primary key  
    
    
    # path('employee',views.Employee.as_view()),  #class based url endpoints
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()),

    path('',include(router.urls)),

    path('blogs/',views.BlogViews.as_view()),
    path('Comment/',views.CommentView.as_view()),

    path('blogs/<int:pk>',views.BlogsDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentDetilView.as_view()),

]


