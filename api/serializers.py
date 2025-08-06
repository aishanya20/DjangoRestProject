from rest_framework import serializers
from students.models import Students
from employee.models import Employee


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields="__all__"    #__all__ means all the data which needed to be serialized

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"