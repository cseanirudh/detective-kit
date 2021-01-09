from django.shortcuts import render,redirect
from .models import State,Register,Test
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render (request,"about.html")
def covidu(request):
  state= State.objects.all()
  return render(request,"Covid Updates.html" ,{"state":state})

def ucovedit(request):
 ustate=State.objects.all()
 return render(request,"ucovedit.html",{"ustate":ustate})

def uucovedit(request,id):
    uustate=State.objects.get(id=id)
    if request.method == "POST":

        n = request.POST['confirmed']
        E = request.POST['recovered']
        m = request.POST['deceased']
        uustate.confirmed=n
        uustate.recovered=E
        uustate.deceased=m

        uustate.save()
        return redirect('uucovedit',id)
    return render(request,"uucovedit.html",{"uustate":uustate})

def addstate(request):
    if request.method == "POST":
        location = request.POST['location']
        recovered = request.POST['recovered']
        confirmed= request.POST['confirmed']
        deceased = request.POST['deceased']
        State.objects.create(location=location, confirmed=confirmed, recovered=recovered, deceased=deceased)
        return redirect("ucovedit")
    return render(request,"addstate.html")


def self(request):
    if request.method=="POST":
       gender=request.POST["gender"]
       age = request.POST["age"]
       mobile = request.POST["mobile"]
       dise1 = request.POST["dise1"]
       dise2 = request.POST["dise2"]
       dise3 = request.POST["dise3"]
       dise4 = request.POST["dise4"]
       Test.objects.create(gender=gender, age=age, mobile=mobile, dise1=dise1, dise2=dise2, dise3=dise3, dise4=dise4)
    return render(request,"self.html")


def alogin(request):

    if request.method == "POST":
        u = request.POST["user"]
        p = request.POST['pwd']
        user = auth.authenticate(username=u, password=p)
        if user is not None:
            auth.login(request, user)
            return redirect('ucovedit')
        else:
            messages.info(request, 'invalid details')
            return redirect('alogin')
    else:

      return render(request, 'adminlogin.html')

def Logout(request):
    logout=request
    return redirect('alogin')

def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        location = request.POST["location"]
        Register.objects.create(name=name, email= email, mobile=mobile, location=location)
        return redirect("self")
    return render(request,"register.html")
def Login(request):
    if request.method == "POST":
        name=request.POST["name"]
        mobile = request.POST["mobile"]
        Register.objects.get(name=name, mobile=mobile)

        return redirect('self')


    return render(request,"login.html")


def alltest(request):
   test=Test.objects.all()

   return render(request,"alltest.html",{"test":test})

def allreg(request):
   allreg=Register.objects.all()

   return render(request,"allreg.html",{"allreg":allreg})

def userdetail(request):
    user = Test.objects.all()
    return render(request,"userdetail.html",{"user":user})

def covid(request):
    return render(request,"covid.html")
