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
            
