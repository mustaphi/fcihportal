from django import forms

from .models import Registeration,Complaint
class SigninForm(forms.ModelForm):
	class Meta:
		model = Registeration
		fields = ['Fname','Mname','Lname', 'Password']
		widgets={'Password':forms.PasswordInput}

class SigninFormAdmin(forms.ModelForm):
	class Meta:
		model = Registeration
		fields = ['Fname','Mname','Lname', 'Password','Professor','Registered']
		widgets={'Password':forms.PasswordInput}

class Complainform(forms.ModelForm):
	class Meta:
		model=Complaint
		fields='__all__'
