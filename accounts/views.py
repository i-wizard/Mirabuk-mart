from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request): #fetch all the inputs used through tyhe post method, then import models... so that ypu can save the users data to database
   if request.method=='POST':
         first_name=request.POST['first_name']
         last_name=request.POST['last_name']
         username=request.POST['user_name']
         email=request.POST['email']
         password1=request.POST['password1']
         password2=request.POST['password2']
         #create model now along with this newly created variables
         if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,"username taken")
               return redirect("register.html")
            elif User.objects.filter(email=email).exists():
               print("daves not matching")
               messages.info(request,"email taken")
               return redirect("register.html")
            else:
               

               user= User.objects.create_user(username=username, password=password1, email=email, first_name= first_name, last_name= last_name)
               user.save() #this will save the user
               print('User created successfully')
               return redirect('login.html')
         else:
            print("password not matching")
            messages.info(request,"password not matching")
            return redirect("register.html")
         return redirect('/') #import redirect...so that this function can work, this redirect will take user back to the homepage after submiting
   else:
         return render(request, 'register.html')
def login(request):
   if request.method=="POST":
      password=request.POST['password']
      username=request.POST['username']

      user=auth.authenticate(username=username, password=password)
      if user is not None:
         auth.login(request, user)
         return redirect('/')
      else:
         messages.error(request,'wrong username or password')
         return redirect('login.html')

   else:  
      return render(request,'login.html')
def logout(request):
   auth.logout(request)
   return redirect('/')
