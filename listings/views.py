from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def index(request):
	#Get all listings from DB.
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)

	paginator = Paginator(listings, 6)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)

	#Generate list to the view.
	context = {
		'listings' : paged_listings
	}

	return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
	return render(request, 'listings/listing.html')


def search(request):
	return render(request, 'listings/search.html')