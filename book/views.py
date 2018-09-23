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
	store = [i.store.name for i in books]
	rating = [i.rating for i in books]
	review_value = [i.review_value for i in books]
	price =  [i.price for i in books]
	sale = [i.sale for i in books]
	isbn = [i.ISBN for i in books]
	response = {}
	response['store'] = store
	response['rating'] = rating
	response['review_value'] = review_value
	response['price'] = price
	response['sale'] = sale
	response['isbn'] = isbn
	print(response)
	# return JsonResponse({'response':response,})
	return render(request,'display.html')