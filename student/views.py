from django.shortcuts import render

# Create your views here.
"""def home(request):
    return render(request,'home.html',context=None)
    return render(request,'home.html',context=None)"""

def student_login(request):
    return render(request,'account/student_login.html') 

def student_signup(request):
    return render(request,'account/student_signup.html') 
       