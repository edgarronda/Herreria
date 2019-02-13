from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from workers.models import Worker
from listings.choices import price_choices, listingtype_choices, state_choices

# Create your views here.
def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

	context = {
		'listings': listings,
		'state_choices': state_choices,
		'listingtype_choices': listingtype_choices,
		'price_choices': price_choices
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
	
