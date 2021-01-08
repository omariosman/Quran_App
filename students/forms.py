from django import forms
from .models import Shaikh, Student, Student_Class


class Student_Class_Form(forms.ModelForm):
    class Meta:
        model = Student_Class
        fields = ['student_code']
        
 