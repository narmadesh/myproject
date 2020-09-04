from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from roles.models import Users, Leave_Application
def index(request):
    return render(request,"roles/login.html")

def login(request):
	email=request.POST.get('email')
	role=request.POST.get('role')
	password=request.POST.get('password')
	login=Users.objects.filter(email=email, role=role, password=password, status='Enabled')
	applications=Leave_Application.objects.all()
	if login.count()>0:
		request.session['email']=email
		request.session['role']=role
		if request.session.get('role')=='Admin':
			return render(request, "roles/admin.html")
		elif request.session.get('role')=='Manager':
			return render(request, "roles/manager.html",{'app':applications})
		else:
			return render(request, "roles/employee.html")
	else:
		return render(request, "roles/login.html", {'message':'Invalid Credentials'})


def logout(request):
	del request.session['email']
	del request.session['role']
	return render(request,"roles/login.html",{'message':'You have been logged out succesfully'})

def create_users(request):
	email=request.POST.get('email')
	role=request.POST.get('role')
	password=request.POST.get('password')
	created_at=datetime.now()
	status='Enabled'
	get=Users.objects.filter(email=email, role=role)
	if get.count()>0:
		return render(request, "roles/admin.html",{'message':'User already registered with this email'})
	else:
		Users(email=email, role=role, password=password, status=status, created_at=created_at).save()
		return render(request, "roles/admin.html",{'message':'User Created Succesfully'})



def home(request):
	if request.session.get('role')=='Admin':
		return render(request, "roles/admin.html")
	elif request.session.get('role')=='Manager':
		applications=Leave_Application.objects.all()
		return render(request, "roles/manager.html",{'app':applications})
	else:
		return render(request,"roles/employee.html")


def apply(request):
	start_date=request.POST.get('start_date')
	end_date=request.POST.get('end_date')
	description=request.POST.get('description')
	leave_avail=request.POST.get('leave_avail')
	status='Pending'
	applied_on=datetime.now()
	applied_by=request.session.get('email')
	Leave_Application(start_date=start_date, end_date=end_date, description=description, leave_avail=leave_avail, status=status, applied_on=applied_on, applied_by=applied_by).save()
	return render(request,"roles/employee.html",{'message':'Your application is submitted succesfully'})



def view_app(request):
	if request.session.get('role') == 'Employee':
		email=request.session.get('email')
		view=Leave_Application.objects.filter(applied_by=email)
		if view.count()>0:
			return render(request,"roles/view_app.html",{'view_app':view})
		else:
			return render(request,"roles/view_app.html",{'message':'You have not applied for any job'})
	

def approve(request):
	update_id=request.POST.get('app_id')
	update=Leave_Application.objects.get(id=update_id)
	update.status='Approved'
	update.approved_by=request.session.get('email')
	update.save()
	applications=Leave_Application.objects.all()
	return render(request,"roles/manager.html",{'message':'Application is approved','app':applications})


def users_list(request):
	users=Users.objects.all().exclude(role='Admin')
	return render(request,"roles/users_list.html",{'users':users})


def user_status(request):
	user_id=request.POST.get('user_id')
	if request.POST.get('enable'):
		user=Users.objects.get(id=user_id)
		user.status='Enabled'
		user.save()
		users=Users.objects.all().exclude(role='Admin')
		return render(request,"roles/users_list.html",{'users':users})
	
	else:
		user=Users.objects.get(id=user_id)
		user.status='Disabled'
		user.save()
		users=Users.objects.all().exclude(role='Admin')
		return render(request,"roles/users_list.html",{'users':users})



def applications(request):
	view_app=Leave_Application.objects.all()
	return render(request,"roles/applications.html",{'view_app':view_app})