from django.db import models

# Create your models here.
class State(models.Model):
    location=models.CharField(max_length=50,null=True)
    recovered=models.IntegerField(null=True)
    confirmed = models.IntegerField(null=True)
    deceased= models.IntegerField(null=True)
    def __str__(self):
       return self.location


class Register(models.Model):
    name=models.CharField(max_length=50, null=True)
    mobile=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    location=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

class Test(models.Model):

    gender=models.CharField(max_length=30,null=True)
    age=models.IntegerField(null=True)
    mobile = models.IntegerField(null=True)
    dise1=models.CharField(max_length=100,null=True)
    dise2 = models.CharField(max_length=100, null=True)
    dise3 = models.CharField(max_length=100, null=True)
    dise4 = models.CharField(max_length=100, null=True)

class login(models.Model):
    name = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(null=True)
    def __str__(self):
        return self.name