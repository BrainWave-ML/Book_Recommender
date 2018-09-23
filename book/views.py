from django.shortcuts import render
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

def home(request):
    return render(request,'home.html')

@csrf_exempt
def display_books(request):
	string = request.POST.get('bname')
	name = string.upper()
	books = Book.objects.filter(name= name)
	r = []
	for i in books:
		response = {}
		response['store'] = i.store.name 
		response['rating'] = i.rating
		response['review_value'] = i.review_value
		response['price'] = i.price
		response['sale'] = i.sale
		response['url'] = i.url
		response['delivery_time'] = i.delivery_time
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
			'price_1':t[0]['price'],
			'rating_1':t[0]['rating'],
			'review_1':t[0]['review_value'],
			'store_1':t[0]['store'],
			'delivery_1':t[0]['delivery_time'],
			'sale_1':t[0]['sale'],
			'url_1':t[0]['url'],
			'price_2':t[1]['price'],
			'rating_2':t[1]['rating'],
			'review_2':t[1]['review_value'],
			'store_2':t[1]['store'],
			'delivery_2':t[1]['delivery_time'],
			'sale_2':t[1]['sale'],
			'url_2':t[1]['url'],

		})