from django.views import View
from django.shortcuts import render
from .models import Student

class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'students.html', {'students': students})