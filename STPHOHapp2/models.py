from django.db import models

class ProjectYear(models.Model):
     name = models.CharField(max_length=100)

     def __str__(self):
         return self.name

class AllProject(models.Model):
    projectname = models.CharField(max_length=225)
    thedate = models.CharField(max_length=100) 
    projectime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        result = self.projectname + "created on" + self.thedate
        return result

class Volunteer(models.Model):
    firstname = models.CharField(max_length=125)
    lastname = models.CharField(max_length=125)
    address = models.CharField(max_length=125)
    Phonenumber = models.CharField(max_length=125)
    gender = models.CharField(max_length=125)

    def __str__(self):
        return self.firstname + self.lastname