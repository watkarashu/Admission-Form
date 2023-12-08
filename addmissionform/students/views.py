from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from students.models import Students
from django.template import loader
from django.urls import reverse


# Create your views here.
def students(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        fathername=request.POST.get('fathername')
        mothername=request.POST.get('mothername')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        address=request.POST.get('address')
        fathermobilenumber=request.POST.get('fathermobilenumber')
        mothermobilenumber=request.POST.get('mothermobilenumber')
        gender=request.POST.get('gender')
        a=Students(firstname=firstname,lastname=lastname,fathername=fathername,mothername=mothername,dob=dob,age=age,address=address,fathermobilenumber=fathermobilenumber,mothermobilenumber=mothermobilenumber,gender=gender)
        a.save()
    return render(request,"index.html")


def datatable(request):
    myhome = Students.objects.all().values()
    template = loader.get_template('datatable.html')
    context={
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request))


def delete(request,id):
    mystudents=Students.objects.get(id=id)
    mystudents.delete()
    return HttpResponseRedirect(reverse('datatable'))


def update(request,id):
    myhome=Students.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    fathername=request.POST['fathername']
    mothername=request.POST['mothername']
    dob=request.POST['dob']
    age=request.POST['age']
    address=request.POST['address']
    fathermobilenumber=request.POST['fathermobilenumber']
    mothermobilenumber=request.POST['mothermobilenumber']
    gender=request.POST['gender']
    myhome=Students.objects.get(id=id)
    myhome.firstname = firstname
    myhome.lastname = lastname
    myhome.fathername = fathername
    myhome.mothername = mothername
    myhome.dob = dob
    myhome.age = age
    myhome.address = address
    myhome.fathermobilenumber = fathermobilenumber
    myhome.mothermobilenumber = mothermobilenumber
    myhome.gender = gender
    myhome.save()
    return HttpResponseRedirect(reverse('datatable'))


def male(request):
    myhome = Students.objects.filter(gender="Male").values()
    template = loader.get_template('male.html')
    context={
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request))


def female(request):
    myhome = Students.objects.filter(gender="Female").values()
    template = loader.get_template('female.html')
    context={
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request))