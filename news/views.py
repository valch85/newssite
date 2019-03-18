from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.

def index(request):
    latest_news_list = News.objects.order_by('-pub_date')[:5]
    context = {'latest_news_list': latest_news_list}
    return render(request, 'news/index.html', context)


def detail(request, news_id):
    #return HttpResponse("You're looking at news %s." % news_id)
    return HttpResponse("You're looking at news %s." % news_id)

