appname : fscohort

    ''' fscohort/views.py'''

            from django.shortcuts import render
            from django.http import HttpResponse
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



   ''' fscohort/templates/fscohort/base.html '''
   
                <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>cw student app</title>
            </head>

            <body>
                {% block content %}
                {% endblock content %}    
            </body>

            </html>

    ''' fscohort/templates/fscohort/home.html '''

        {% extends 'fscohort/base.html' %}

            {% block content %}

                <h1>
                    <center>
                        CANCAĞAZIM
                    </center>
                </h1>

            {% endblock content %}

    ''' fscohort/templates/fscohort/student_list.html '''

        {% extends 'fscohort/base.html' %}


                {% block content %}
                <h1>öğrenci listesi</h1>
                <ul>
                
                {% for i in students %}
                <li>{{i}}</li>

                {% endfor %}
                
                    
                </ul>

                {% endblock content %}
 # add data to database
  create forms in fscohort

'''' fscohort/forms.py'''

from django import forms 
from django.forms import fields      
from .models import Student

class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = "__all__"

write after forms.py
goto views.py to add a student in the database
''''fscohort/views.py''' 
 1_ import your form (student_form)
  
   from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import student_form

# Create your views here.
def home(request):
    return render(request, 'fscohort/home.html')

def student_list(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, 'fscohort/student_list.html', context)

# create_add işlemleri için:    
''''
     from django import forms 
    from django.forms import fields      
    from .models import Student

class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = "__all__"
"""" form u böyle hazırlamıştık. (model dekinin aynısı modelle karşılaştır.)
# şimdi views.py geliyoruz student_add işlrmiya pacağız
# fscohort/views.py :
 from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# Create your views here.
{% comment %} def home(request):
    return render(request, 'fscohort/home.html')

def student_list(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, 'fscohort/student_list.html', context) {% endcomment %}

def student_add(request):
    form = StudentForm()
    if request.models == "POST" : 
        form = StudentForm(request.POST)
        if form.is_valid():
             form.save()    
    
    context = {
        "form" : form,        
    }  
    return render(request, 'fscohort/student_add.html', context)

student_add fonsiyonumuzu yazdıktansonra: "
"
fscohort/templates/fscohort/ a student_add.html oluşturuyoruz. 
""""
{% extends 'fscohort/base.html' %}

{% block content %}
{% csrf_token %}

 <form action="" method="POST">

    {{form.as_p}}

    <input type="submit" value="Add">


 </form>

{% endblock content %}

sonra : urls git ekleme yap:
""""
from django.urls import path
from .views import home, student_list, student_add

urlpatterns = [
   
    path('', home, name='home'),
    path('student_list/', student_list, name='list'),
    path('student_add/', student_add, name='add')
]


             
