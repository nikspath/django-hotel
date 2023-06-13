from django.shortcuts import render,redirect
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


def admin_register(request):
	print("ssssss",request.POST.get('password'))
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user_obj = User.objects.filter(username=username)
		if not user_obj.exists():
			user=User.objects.create(username=username,is_staff=True,is_active=True,is_superuser=True)
			user.set_password(password)	
			user.save()
			messages.success(request,"user saved")
			return redirect("/tpl/admin-login/")
		else:
			messages.warning(request,"already exist")


	return render(request,'register.html')	