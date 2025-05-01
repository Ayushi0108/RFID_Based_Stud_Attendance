from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Record, Stud
# Create your views here.
def start(request):
    return redirect('login')
    # return HttpResponse("<a href='/login'>Login</a>")
    
def logout(request):
    auth.logout(request)
    return redirect('login')

def error_404(request, *args, **kwargs):
    return render(request,'user_authentication/404.html')

def error_500(request,*args, **kwargs):
    return render(request,'user_authentication/500.html')


def login(request):
    if request.user.is_authenticated:
        user = request.user.username
        username = str(user)
        if Record.objects.filter(email=username):
            return redirect('teacher_dashboard')
        elif Stud.objects.filter(email=username):
            return redirect('student_dashboard')
            # return HttpResponse("You are student:) <br/><a href='/logout'>Logout</a><br/><a href='/change_pass'>change password</a>")
        else:
            return redirect('/admin')
            return HttpResponse("WHo are you ? <br/><a href='/logout'>Logout</a><br/>")
        # return HttpResponse("<a href='/logout'>Logout</a><a href='/change_pass'>change password</a>")

    if request.method == 'POST':        
        email = request.POST['email_field']
        password = request.POST['pass_field']
        user  = auth.authenticate(username=email, password = password)
        if user is not None:
            ob = User.objects.get(username = user)
            print(ob.is_superuser)            
            auth.login(request, user)
            print(user,type(user))
            return redirect('login')               
        else:
            # messages.error(request, 'Incorrect Username or Password !')
            return render(request, 'user_authentication/new_login.html',{'message':"Incorrect Username or Password !"})
            # return HttpResponse("<a href='/logout'>Logout</a><a href='/change_pass'>change password</a>")# go to dashboard
    return render(request, 'user_authentication/new_login.html')

def change_pass(request):
    if request.method == 'POST' and request.user.is_authenticated:                
        #check old password        
        if auth.authenticate(username = request.user.username, password = request.POST['old_pass_field']):
            if request.POST['new_pass_field_1'] == request.POST['new_pass_field_2']:
                u = request.user
                print(request.POST['new_pass_field_1'])
                u.set_password(request.POST['new_pass_field_1'])
                u.save()

                # messages.success(request, 'Password Changed successfully !')
                message = "Password Changed Successfully !"
            else:
                #messages.error(request, 'Confirm Password does not match')
                message = "Confirm Password does not match !"
        else:
            # messages.error(request, 'Invalid Old password') 
            message = "Invalid Old Password !"
        return render(request, 'user_authentication/change_pass.html',{'message':message})
        #check pass1 and pass2        
    if(request.user.is_authenticated):
        return render(request, 'user_authentication/change_pass.html')
    



