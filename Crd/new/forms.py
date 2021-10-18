from django import  forms
from  .models import  StudentReg

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentReg
        fields = ['name','age','email','password']
