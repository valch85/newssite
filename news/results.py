from django.shortcuts import render, get_object_or_404
from .models import News
from .documents import NewsDocument

# Making search from the search_string param
def results(request):
    news_list_by_name = NewsDocument.search().query("match", news_name=request.POST['search_string'])
    news_list_by_desc = NewsDocument.search().query("match", news_desc=request.POST['search_string'])
    context = {'news_list_by_name': news_list_by_name.to_queryset(), 'news_list_by_desc': news_list_by_desc.to_queryset()}
    return render(request, 'news/results.html', context)

def detail(request, news_id):
    new = get_object_or_404(News, pk=news_id)
    return render(request, 'news/detail.html', {'new': new})