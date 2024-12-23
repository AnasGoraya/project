from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout

# Create your views here.
def index(request):
    return render(request,"index.html")


def signup(request):
    # For create signup(user)
    if request.method=='POST':
        uname = request.POST.get('username')
        email  = request.POST.get('email') 
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        #print on terminal
        print(uname,email,password,password1)
        # fro check pass is = or not = confrim pass
        if password != password1:
            return HttpResponse(" Please confirm Password ")

        signup_user = User.objects.create_user(uname,email,password1)
        signup_user.save()
        return redirect('login')

    return render(request,'signup.html')


def login(request):
    if request.method=='POST':
        uname= request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request,username = uname, password = password )
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            return HttpResponse(' Please Check Username and Password again! ')
    return render(request,"login.html")






