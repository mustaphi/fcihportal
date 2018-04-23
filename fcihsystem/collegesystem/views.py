# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import SigninForm,Complainform
from .models import Registeration,Complaint,Registeration_Course,Course,CoursesRequirements
from django.template import loader
from django.http import *


# Create your views here.
def login (request):
    form=SigninForm(request.POST or None)
    context={"form":form}
    if request.method=="POST":
        found=False
        if form.is_valid():
            instance=form.save(commit=False)
            users=Registeration.objects.all()
            for item in users:
                if (item.Fname==instance.Fname) and (item.Mname==instance.Mname) and (item.Lname==instance.Lname) and (item.Password==instance.Password):
                    instance = item
                    found=True
                    break
            if not found:
                    context={"msg":"Invalid Credentials","form":form}
                    return render(request, "login.html", context)
            else:
                    return redirect("/login/"+str(instance.id))
    return render(request,"login.html",context)

def  Register(request,Registeration_id,*args,**kwargs):
    item = Registeration.objects.filter(id=Registeration_id)
    if (request.method=="POST"):
        subjects=list((request.POST).keys())
        del subjects[0]
        if len (subjects)>6:
            return HttpResponse("<h1>You can not register more than 6 courses</h1><br><a href='/login/complaint'>Complain</a>")
        else:
            for subject in subjects:
                reg=Course()
                reg=list(Course.objects.filter(Course_name=subject))
                saving=Registeration_Course()
                saving.Course_Id=reg[0]
                saving.Registeration_Id=item[0]
                saving.save()
            Registeration.objects.filter(id=Registeration_id).update(Registered=True)
            return  HttpResponse("<h1>Submitted</h1><br><a href='/login/complaint'>Complain</a>")
    if len(item) and not item[0].Registered :
        availablecourses=[]
        registeredcourses=Registeration_Course.objects.filter(Registeration_Id=item)
        allcourses=Course.objects.all()
        for course in allcourses:
            pre=CoursesRequirements.objects.filter(CourseId=course)
            if  len(pre) :
                    for regcourse in registeredcourses:
                        if regcourse.Course_Id.Course_name==pre[0].Require:
                            can=True
                            for regcourse in registeredcourses:
                                if regcourse.Course_Id.Course_name==course.Course_name:
                                    can=False
                                    break
                            if can:
                                    availablecourses.append(course)
            else :
                can=True
                for regcourse in registeredcourses:
                    if regcourse.Course_Id.Course_name ==course.Course_name:
                        can=False
                        break
                if can:
                        availablecourses.append(course)
        context = {'courses': availablecourses}
        return render(request, "register.html", context)
    else :
        return  HttpResponse("<h1>You are registered before</h1><br><a href='/login/complaint'>Complain</a>")
def complaint(request):
    form=Complainform(request.POST or None)
    context={'form':form}
    if form.is_valid():
        formdata=form.save(commit=False)
        instance=Complaint()
        instance.Student_id=formdata.Student_id
        instance.Complaint=formdata.Complaint
        instance.save()
        return HttpResponse("<h1>Submitted<h1>")
    return render(request,"complaint.html",context)
