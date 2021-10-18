from django.contrib import admin
from  .models import  StudentReg
# Register your models here.
@admin.register(StudentReg)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','email','password']