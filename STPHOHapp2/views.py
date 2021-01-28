from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import ProjectYear, AllProject, Volunteer


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

    return render(request, 'index.html', {"count":count,"count":countprojecthistory,"count":countvolunteer})

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
def projectresults(request, id=id):
    result = ProjectYear.objects.get(pk=id)
    return render(request, "projectcreated.html", {"result":result})