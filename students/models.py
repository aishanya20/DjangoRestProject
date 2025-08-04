from django.db import models

class Students(models.Model):
    student_id=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)

    def _str_(self):
        return self.name
