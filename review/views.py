from django.shortcuts import render
from book.models import Book
from review.models import Review
from django.http import JsonResponse, HttpResponse

# Create your views here.
def get_reviews(request,id):
	book = Book.objects.get(id=id)
	# book_name = book.name
	reviews = Review.objects.filter(book=book)
	reviews_text = [i.body for i in reviews]
	print(reviews)
	return JsonResponse({'reviews':reviews_text,})
