# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Course, Chapter, Registeration, Registeration_Course, Feedback, LearnercodeRegistry, Batch, \
    Complaint, Result, Test, Testhistory, Studenthistory,CoursesRequirements
from forms import SigninFormAdmin
class SignInAdmin(admin.ModelAdmin):
	form = SigninFormAdmin
admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Registeration,SignInAdmin)
admin.site.register(Registeration_Course)
admin.site.register(Feedback)
admin.site.register(LearnercodeRegistry)
admin.site.register(Batch)
admin.site.register(Complaint)
admin.site.register(Result)
admin.site.register(Test)
admin.site.register(Testhistory)
admin.site.register(Studenthistory)
admin.site.register(CoursesRequirements)
