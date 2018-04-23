# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django import forms

# Create your models here.
class Course (models.Model):
    Course_name=models.CharField(primary_key=True,max_length=250,blank=False,null=False)
    def __unicode__(self):
        return self.Course_name


class Chapter (models.Model):
    Course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    Chapter_name = models.CharField(max_length=250, blank=False, null=False)
    def __unicode__(self):
        return self.Chapter_name+" "

class Registeration(models.Model):
    Fname=models.CharField(max_length=250,blank=False,null=False)
    Mname = models.CharField(max_length=250, blank=False, null=False)
    Lname = models.CharField(max_length=250, blank=False, null=False)
    Password = models.CharField(max_length=50, blank=False, null=False)
    Professor = models.BooleanField()
    Registered=models.BooleanField()
    def __unicode__(self):
        return str(self.Fname)+"  "+str(self.pk)


class Registeration_Course(models.Model):
    Registeration_Id=models.ForeignKey(Registeration,on_delete=models.CASCADE)
    Course_Id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __unicode__(self):
        return str(self.Registeration_Id)+str(self.Course_Id)

class LearnercodeRegistry(models.Model):
    Learnercod=models.CharField(max_length=250,blank=False,null=False)
    def __unicode__(self):
        return str(self.pk)+"  "+self.Learnercod

class Batch(models.Model):
    Name=models.CharField(max_length=250,blank=False,null=False)
    Status=models.CharField(max_length=250,blank=False,null=False)
    Totalohours=models.IntegerField(blank=False,null=False)
    def __unicode__(self):
        return self.Name

class Feedback(models.Model):
    Feedback_Message=models.CharField(max_length=250,blank=False,null=False)
    def __unicode__(self):
        return self.Feedback_Message

class Complaint (models.Model):
    Student_id=models.CharField(max_length=250,blank=False,null=False)
    Complaint=models.CharField(max_length=250,blank=False,null=False)
    def __unicode__(self):
        return self.Student_id+"   "+self.Complaint

class Result (models.Model):
    Student_id=models.ForeignKey(Registeration,on_delete=models.CASCADE)
    Course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    Pass_exam=models.BooleanField()
    Totalmarks=models.IntegerField(blank=False,null=False)
    Paractical=models.IntegerField(blank=False,null=False)
    Theoritical=models.IntegerField(blank=False,null=False)
    def __unicode__(self):
        return self.Student_id+"  "+str(self.Totalmarks)

class Test(models.Model):
    Course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    Student_id=models.ForeignKey(Registeration,on_delete=models.CASCADE)
    Name=models.CharField(max_length=250,blank=False,null=False)
    Practical=models.BooleanField()
    def __unicode__(self):
        return self.Student_id+"  "+self.Course_id+"  "+self.Name


class Studenthistory(models.Model):
    Student_id = models.ForeignKey(Registeration, on_delete=models.CASCADE)
    Test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.Student_id+ "  "+ self.Test_id

class Testhistory(models.Model):
    SHID=models.ForeignKey(Studenthistory,on_delete=models.CASCADE)
    TQN=models.CharField(max_length=250,null=False,blank=False)
    def __unicode__(self):
        return self.SHID +"  "+self.TQN

class CoursesRequirements(models.Model):
    CourseId=models.ForeignKey(Course,on_delete=models.CASCADE,primary_key=True)
    Require=models.CharField(max_length=250,null=False,blank=False)
    def __unicode__(self):
        return str(self.CourseId)