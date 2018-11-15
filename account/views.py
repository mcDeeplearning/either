from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    #사용자가 로그인을 요청했으면?
    if request.method == "POST": 
        form =  AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('question:list')
    
    #로그인을 위한 폼을 요청했을때?
    else:
        form = AuthenticationForm()
    return render(request,'account/login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('question:list')
    pass