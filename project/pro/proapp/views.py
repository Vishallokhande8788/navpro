from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'proapp/home.html')

@login_required
def python_exam(request):
    return render(request, 'proapp/python_exam.html')