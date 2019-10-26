from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
"""def home(request):
    return render(request,'home.html',context=None)
    return render(request,'home.html',context=None)"""



def teacher_login(request):
    return render(request,'account/teacher_login.html') 


       
def teacher_signup(request):
    return render(request,'account/teacher_signup.html') 