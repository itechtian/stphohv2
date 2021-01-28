from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django.contrib.auth.models import User, auth

from django.views.decorators.http import require_http_methods
import random

access= "1H4all"

random_checking = [
                    '.',',',';','/',':','}',']','[','_','=','-',
                   ')','(','*','&','^','%','$','#','@','!','|',"\'",
                   '\"','>','<','~','`','1','2','3','4','5','6','7','8',
                   '9','0'
                   ]

@require_http_methods(["GET", "POST"])
def register_view(request):
    next = request.GET.get('next')
    if request.method == "POST":
        first = request.POST.get('first').lower()
        last = request.POST.get('last').lower()
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        accesscode = request.POST.get('accesscode')
        username = first+str(random.randint(000,100))+"@admin"

        for char in first or last:
            if char in random_checking:
                error = "Please enter a valid name"
                return render(request, 'register.html', {'error':error})

        if password1 != password2:
            password_error = "password mismatched"
            return render(request, 'register.html', {'password_error':password_error})

        elif accesscode != access:
            access_error = "Access denied"
            return render(request, 'register.html', {'access_error':access_error})
        
        # elif User.objects.filter().exists():
        #     user_error = "this name exits here"
        #     return render(request, 'register.html', {'user_error':user_error})

        elif len(password1) < 5:
             user_error = "password to short"
             return render(request, 'register.html', {'user_error':user_error})

            
        user = User.objects.create_user(username= username, password=password1, first_name=first, last_name=last, email=email)
        user.save()
        generatedusername = username
        return render(request, 'register.html',{'generatedusername':generatedusername})
    return render(request, 'register.html')

@require_http_methods(["GET", "POST"])
def login_view(request):
     next = request.GET.get('next')
     if request.method == "POST":
         username = request.POST.get('username').lower()
         password = request.POST.get("password")
         user = authenticate(username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect("/")
         not_user = "you are not authenticated"
         context = ({'not_user':not_user})
         return render(request, 'login.html', context)
     return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("/")

