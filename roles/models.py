from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.
class Users(models.Model):
	email=models.CharField(max_length=50)
	role=models.CharField(max_length=20)
	password=models.CharField(max_length=8)
	status=models.CharField(default="Enabled", max_length=25)
	created_at=models.DateField(default=date.today)
	

class Leave_Application(models.Model):
	start_date=models.DateField(default=date.today)
	end_date=models.DateField(default=date.today)
	description=models.TextField()
	leave_avail=models.IntegerField()
	applied_on=models.DateField(default=date.today)
	approved_on=models.DateField(default=date.today)
	approved_by=models.CharField(max_length=50)
	status=models.CharField(max_length=25)
	applied_by=models.CharField(default='', max_length=50)