from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'fscohort/home.html')

def student_list(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, 'fscohort/student_list.html', context)

def student_add(request):
    form = StudentForm()
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
       
       "form":form     
    }
    
    return render(request, "fscohort/student_add.html", context)
