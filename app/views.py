from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .forms import signupForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User


def index(request):
    return render(request, 'app/main/index.html')

def info(request):
    return render(request, 'app/content/Info.html')

def Performance(request):
    return render(request, 'app/content/Performance.html')

def Applications(request):
    return render(request, 'app/content/Applications.html')    

def hpc(request):
    return render(request, 'app/content/Hpc.html')

def sign_up(request):
    if request.method == "POST":
        fm = signupForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Account Created successfully!")
            fm.save()
            return HttpResponseRedirect('/login/')
        print("Success")
    else:
        print("unSuccess")
        fm = signupForm()
    return render(request,"app/registration/signup.html", {'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,"Logged in successfully !!..")
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,"app/registration/signin.html", {"form":fm})
    else:
        return HttpResponseRedirect('/profile/')      


def user_profile(request):
    if request.user.is_authenticated:
        print("User Authenticatd")
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users=User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users=None
            if fm.is_valid():
                print("Form Validated")
                messages.success(request, "Profile Updated !")
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users=User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users=None
        return render(request,'app/registration/profile.html', {"name":request.user.username, 'form':fm, 'users':users})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    messages.success(request,"Logged out successfully !!..")
    return HttpResponseRedirect('/')
    #return render(request,'app/registration/profile.html',{"form":fm})

def user_changepass(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user = request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request," Password Changed successfully !!..")
            return HttpResponseRedirect('/profile/')
    else:
        fm = PasswordChangeForm(user = request.user)
    return render(request,'app/registration/changepass.html', {"form":fm})

def user_changepass1(request):
    if request.method == "POST":
        fm = SetPasswordForm(user = request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request," Password Changed successfully !!..")
            return HttpResponseRedirect('/profile/')
    else:
        fm = SetPasswordForm(user = request.user)
    return render(request,'app/registration/changepass1.html', {"form":fm})


def user_details(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request,'app/registration/user_details.html',{"form":fm})
    else:
        return HttpResponseRedirect('/login/')