from django.shortcuts import render
from django.http import HttpResponse

from .models import User
from sensor.models import Readings
# Create your views here.

def index(request):
	return render(request, 'terminal/index.html', context=None)

def logs(request):
	uname = request.POST['uname']
	pwd = request.POST['pwd']

	try:
		usr = User.objects.get(uname=uname, pwd=pwd)
	except User.DoesNotExist:
		return HttpResponse("<h1 style='color:red'>Incorrect Credentials</h1>")
	else:
		records = Readings.objects.all()
		return render(request, 'terminal/logs.html', context={'uname':uname, 'records':records})


def clear(request):
	records = Readings.objects.all()

	for obj in records:
		obj.delete()
	
	return HttpResponse("Logs Cleared")
