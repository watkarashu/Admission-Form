from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('',views.students,name='students'),
    path('datatable',views.datatable,name='datatable'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('male',views.male,name='male'),
    path('female',views.female,name='female'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),
]
