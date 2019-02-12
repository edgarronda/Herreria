from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from workers.models import Worker

# Create your views here.
def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

	context = {
		'listings': listings
	}	

	return render(request, 'pages/index.html', context)


def about(request):
	#Get all workers.
	workers = Worker.objects.order_by('-hire_date')

	#Get MVP Workers
	mvp_workers = Worker.objects.all().filter(is_mvp=True)

	context = {
		'workers': workers,
		'mvp_workers': mvp_workers
	}

	return render(request, 'pages/about.html', context)
	
