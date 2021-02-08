from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import ProjectYear, AllProject, Volunteer
from django.db.models import Q
from django.contrib.auth.models import User, auth 
from django.contrib.auth.hashers import check_password
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    
)
    



@login_required
def searchfunc(request): 
    if request.method == "POST":
        query = request.POST.get("q")
        result1 = ProjectYear.objects.filter(Q(name__contains=query))
        result2 = AllProject.objects.filter(Q(projectname__contains=query))
        result3 = Volunteer.objects.filter(Q(firstname__contains=query))
        return render(request, 'searchpage.html', {"result1":result1,"result2":result2,"result3":result3})
    return render(request, "searchpage.html")
    

@login_required
def createProjectfunc(request):
    if request.method == "POST":
        names = request.POST.get("foldername")
        foldername = ProjectYear(name= names)
        foldername.save()
        return redirect("/")

@login_required
def home(request):
    count = AllProject.objects.count()
    countprojecthistory = ProjectYear.objects.count()
    countvolunteer = Volunteer.objects.count()

    if request.method == "POST":
        projectname = request.POST.get("projectname")
        projectdate = request.POST.get("projectdate")

        projects = AllProject(projectname = projectname, thedate = projectdate)
        projects.save()
        return redirect("/")

    return render(request, 'index.html',{
        "count":count,
        "countfiles":countprojecthistory,
        "count":countvolunteer,
       
    })

@login_required
def openfiles(request):
    folder = ProjectYear.objects.all()
    if request.method == "POST":
        names = request.POST.get("foldername")
        foldername = ProjectYear(name= names)
        foldername.save()
        return redirect("/openfiles")
    return render(request, 'openfiles.html', {"folder":folder})



@login_required
def deletefunc(request,id=id):
    deletefunct = ProjectYear.objects.get(pk=id)
    if request.method == "POST":
        passworded = request.POST.get("password")
        check = check_password(passworded,encoded)
        
        if check is True:
            deletefunct.delete()
            return redirect("/openfiles")
        return HttpResponse("Wrong password")
    return render(request, "delete.html", {"folder":deletefunct})
       
    


@login_required
def projectresults(request, id=id):
    result = ProjectYear.objects.get(pk=id)
    return render(request, "projectcreated.html", {"result":result})