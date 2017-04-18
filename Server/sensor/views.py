from django.shortcuts import render
from django.utils import timezone
from .models import Readings
# Create your views here.

def index(request):
	return render(request, 'sensor/index.html', context=None)


def fire(request):

	if request.method == "POST":
		read = request.POST['val']

		obj = Readings(sensor_type="Fire", reading=read, time=timezone.now())
		obj.save()

	return render(request, 'sensor/fire.html', context=None)


def tremor(request):

	if request.method == "POST":
		read = request.POST['val']

		obj = Readings(sensor_type="Tremor", reading=read, time=timezone.now())
		obj.save()

	return render(request, 'sensor/tremor.html', context=None)


