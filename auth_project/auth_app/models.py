from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False,blank=True,null=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
        
    
    def __str__(self):
        return self.title
    
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name