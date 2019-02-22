from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
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


		#Worker already have inquery.
		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(listing_id =listing_id, user_id = user_id)
			if has_contacted:
				messages.error(request, 'Ya solicitaste una cotizacion para este producto.')
				return redirect('/listings/'+listing_id)


		contact = Contact(listing = listing, listing_id = listing_id, name = name, email = email, 
		phone = phone, message = message, user_id = user_id)

		contact.save()

		#Send Email
		send_mail(
			'Cotizacion de Producto',
			'Se requiere una cotizacion para el producto: ' + listing + '. Ingresa al panel para mas informacion',
			'test_email@gmail.com',
			[worker_email, 'trabajador@gmail.com'],
			fail_silently = False
			)



		messages.success(request, 'Tu informacion a sido enviada, pronto se te contactara.')

		return redirect('/listings/'+listing_id)