from django.contrib import admin
from django.urls import path,include
from news import views

urlpatterns = [
    path('set_news',views.set_news),
    path('setauthor',views.set_autor),
    path('getAuthorNews',views.getAuthorNews),
    path('getAllNew',views.getAllNews),
    path('DeleteNews',views.DeleteNews),
    path('UpdateNews',views.UpdateNews),
]
