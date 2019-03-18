from django.shortcuts import render, get_object_or_404
from .models import News

# Create your views here.

def index(request):
    latest_news_list = News.objects.order_by('-pub_date')[:5]
    context = {'latest_news_list': latest_news_list}
    return render(request, 'news/index.html', context)


def detail(request, news_id):
    new = get_object_or_404(News, pk=news_id)
    return render(request, 'news/detail.html', {'new': new})

