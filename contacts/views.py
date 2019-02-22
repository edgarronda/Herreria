from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


# Create your views here.
def contact(request):
	if request.method == 'POST':
		listing_id = request.POST['listing_id']
		listing = request.POST['listing']
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		worker_email = request.POST['worker_email']

		contact = Contact(listing = listing, listing_id = listing_id, name = name, email = email, 
		phone = phone, message = message, user_id = user_id)

		contact.save()

		messages.success(request, 'Tu informacion a sido enviada, pronto se te contactara.')

		return redirect('/listings/'+listing_id)