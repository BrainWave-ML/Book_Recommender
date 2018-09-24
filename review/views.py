from django.shortcuts import render
from book.models import Book
from review.models import Review
from django.http import JsonResponse, HttpResponse
from sentiment_analysis import pred_sentiment
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_reviews(request,id):
	book = Book.objects.get(id=id)
	# book_name = book.name
	reviews = Review.objects.filter(book=book)
	reviews_text = [i.body for i in reviews]
	print(reviews)
	cum_sent = 0
	for i in reviews_text:
		sent = pred_sentiment(i)
		print(sent)
		cum_sent = cum_sent + int(sent)
	print(cum_sent)

	cum_sent = cum_sent/len(reviews_text)
	print(cum_sent)
	return JsonResponse({'reviews':reviews_text,'sentiment':cum_sent})

@csrf_exempt
def sentiment(request):
	if request.method =='POST':
		text = request.POST.get('text')
		sent = pred_sentiment(text)
		sent = int(sent)
		print(sent)
		return render(request,'sentiment_post.html',{'sent':sent,})
	else:
		return render(request,'sentiment.html')