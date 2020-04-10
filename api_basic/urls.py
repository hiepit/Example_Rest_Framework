
from django.contrib import admin
from django.urls import path
from .views import Article_list, article_detail

urlpatterns = [
    path('article', Article_list,),
    path('article/<int:pk>', article_detail,)
]
