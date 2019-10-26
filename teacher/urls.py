
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [

    #path('',view=views.home,name="home"),
    #path('studentlogin',view=views.student_login,name="studentlogin"),
    path('teacher',view=views.teacher_login,name="teacher"),
    #path('teacherlogin',view=views.teacher_login,name="teacherlogin"),
    path('teacher',view=views.teacher_signup,name="teacher"),
   
]
