


from django.urls import path
from  . import  views

urlpatterns = [

    path('', views.Home , name = "home"),
    path('<int:id>', views.update, name="update"),
    path('delete/<int:id>' ,views.delete,name ="Deletedata"),

]
