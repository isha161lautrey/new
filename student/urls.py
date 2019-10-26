from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [

    #path('',view=views.home,name="home"),
    path('student',view=views.student_login,name="student"),
    #path('teacherlogin',view=views.teacher_login,name="teacherlogin"),
    path('student',view=views.student_signup,name="student"),
    #path('teachersignup',view=views.teacher_signup,name="teachersignup"),
   
]
