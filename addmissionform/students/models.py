from django.db import models

# Create your models here.
class Students(models.Model):
    firstname=models.CharField(max_length=220)
    lastname=models.CharField(max_length=220)
    fathername=models.CharField(max_length=220)
    mothername=models.CharField(max_length=220)
    dob=models.DateField()
    age=models.IntegerField()
    address=models.CharField(max_length=300)
    fathermobilenumber=models.CharField(max_length=220)
    mothermobilenumber=models.CharField(max_length=220)
    '''GENDER_CHOICE=[
        ('M','Male'),
        ('F','Female'),
        ]'''
    gender=models.CharField(max_length=220)