from django.urls import path
from . import views
from . import results

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', results.results, name='results'),
    path('<int:news_id>/', views.detail, name='detail'),
]
