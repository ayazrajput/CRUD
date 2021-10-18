from django.shortcuts import render
from django.http import  HttpResponseRedirect
from  .forms import  StudentForm
from  .models import StudentReg
# Create your views here.
def Home(request):
    fm = StudentForm()
    if request.method == "POST":
        frm = StudentForm(request.POST)
        if frm.is_valid():
            name = frm.cleaned_data['name']
            age = frm.cleaned_data['age']
            email = frm.cleaned_data['email']
            password = frm.cleaned_data['password']
            reg =StudentReg(name = name , age =age , email =  email , password = password)
            reg.save()


        else:
            fm = StudentForm()

    else:
        fm = StudentForm()

    Data = StudentReg.objects.all()
    return  render(request ,"home.html" ,{'form':fm ,"data":Data})

def delete(request ,id):

    if request.method == "POST":
        de = StudentReg.objects.get(pk = id)
        de.delete()
        return HttpResponseRedirect('/')

def update(request,id):
     if request.method =="POST":
         pi = StudentReg.objects.get(pk=id)
         vi = StudentForm(request.POST , instance=pi)
         if vi.is_valid():
             vi.save()
     else:
         pi = StudentReg.objects.get(pk=id)
         vi = StudentForm(instance=pi)


     return render(request,'update.html' ,{"id":vi} )