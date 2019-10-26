
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    #path('',include('st_portal.urls')),
    path('',include('student.urls')),
    path('',include('teacher.urls')),
]
