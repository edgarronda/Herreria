from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


# Create your views here.
def register(request):
	if request.method == 'POST':
		#Get form values
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password_two = request.POST['password2']

		#Validate if passwords match
		if password == password_two:
			#Validations
			if User.objects.filter(username=username).exists():
				messages.error(request, 'El usuario ya existe.')
				return redirect('register')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request, 'El correo ya existe.')
					return redirect('register')
				else:
					user = User.objects.create_user(username=username, password=password, email=email,
						first_name=first_name, last_name=last_name)
					#login
					# auth.login(request, user)
					# messages.sucess(request, 'Se ha iniciado sesion.')
					# return redirect('index')
					user.save()
					messages.success(request, 'Se ha resgistrado tu cuenta.')
					return redirect('login')


		else:
			messages.error(request, 'Las contrasenas no coinciden.')
			return redirect('register')
	else:
		return render(request, 'accounts/register.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password=password)

		if user is not None:
			auth.login(request, user)
			messages.success(request, 'Haz iniciado sesion.')
			return redirect('dashboard')
		else:
			messages.error(request, 'Usuario no existe')
			return redirect('login')
	else:
		return render(request, 'accounts/login.html')


def dashboard(request):
	user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)

	context = {
		'contacts': user_contacts
	}

	return render(request, 'accounts/dashboard.html', context)


def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request, 'Se ha cerrado la sesion')
		return redirect('index')


