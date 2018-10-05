from django.shortcuts import render, redirect
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,'home.html')

@csrf_exempt
def display_books(request):
	string = request.POST.get('bname')
	name = string.upper()
	print("count is:->")
	print(Book.objects.filter(name= name).count())
	if(Book.objects.filter(name= name).count()==0):
		t = [{},{}]
		t[0]['name'] = 'Not Available'
		t[0]['author'] = 'Unknown'

		t[0]['price'] = 0
		t[0]['rating'] = 0
		t[0]['review_value'] = 0
		t[0]['store'] = 0
		t[0]['delivery_time'] = 9999
		t[0]['sale'] = 0
		t[0]['url'] = '/home'
		t[0]['image'] = '/static/default_book.gif'

		t[1]['price'] = 0
		t[1]['rating'] = 0
		t[1]['review_value'] = 0
		t[1]['store'] = 0
		t[1]['delivery_time'] = 9999
		t[1]['sale'] = 0
		t[1]['url'] = '/home'
		t[1]['image'] = '/static/default_book.gif'
	else:
		books = Book.objects.filter(name=name)
		r = []
		for i in books:
			response = {}
			response['name'] = i.name
			response['author'] = i.author
			response['store'] = i.store.name 
			response['rating'] = i.rating
			response['review_value'] = i.review_value
			response['price'] = i.price
			response['sale'] = i.sale
			response['url'] = i.url
			response['delivery_time'] = i.delivery_time
			response['image'] = i.image
			r.append(response)
		print(r)
		comp1 = r[0]['price']+r[0]['delivery_time']+50-(10*r[0]['rating'])+90-(30*r[0]['review_value'])+(1/r[0]['sale'])
		comp2 = r[1]['price']+r[1]['delivery_time']+50-(10*r[1]['rating'])+90-(30*r[1]['review_value'])+(1/r[1]['sale'])
	
		if(comp1<comp2):
			index = 0
		else:
			index = 1

		recommended = r[index]
		other = r[1-index]


		t = []
		t.append(other)
		t.append(recommended)
	
	return render(request,'display.html',
		{
			'name': t[0]['name'],
			'author': t[0]['author'],

			'price_1':t[0]['price'],
			'rating_1':t[0]['rating'],
			'review_1':t[0]['review_value'],
			'store_1':t[0]['store'],
			'delivery_1':t[0]['delivery_time'],
			'sale_1':t[0]['sale'],
			'url_1':t[0]['url'],
			'image_1':t[0]['image'],

			'price_2':t[1]['price'],
			'rating_2':t[1]['rating'],
			'review_2':t[1]['review_value'],
			'store_2':t[1]['store'],
			'delivery_2':t[1]['delivery_time'],
			'sale_2':t[1]['sale'],
			'url_2':t[1]['url'],
			'image_2':t[1]['image'],

		})

def register(request):
	if request.method == 'POST':		
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
		else:
			return render(request,'register.html',{'error': form.errors})
		return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form': form,'error':''})

def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if(user == None):
			return render(request, 'login.html',{'error':'Invalid credentials'})		
		login(request, user)
		return redirect('home')
	return render(request, 'login.html',{'error':''})