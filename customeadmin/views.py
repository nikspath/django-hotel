from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_admin(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user_obj = User.objects.filter(username=username)
		if not user_obj.exists():
			messages.warning(request,"user not found")
			return render(request,'login.html')
		user = authenticate(username=username,password=password)
		if not user:
			messages.warning(request,"user and password not match not found")
			return render(request,'login.html')
		login(request,user)
		return render(request, 'dashboard.html')
	return render(request,'login.html')


def logout_admin(request):
	logout(request)
	return render(request,'login.html') 	