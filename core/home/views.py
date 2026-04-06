from django.views import View
from django.shortcuts import render, redirect
from .models import Student

class StudentCreateView(View):
    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        return redirect('success')
    
def success_view(request):
    return render(request, 'success.html')