from django.urls import path
from . import views
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
# from .views import PostListView
# from .views import add_comment

urlpatterns = [
	path('', views.index,name='index'),
    path('blogdetails/<int:id>/', views.blogdetails, name='blogdetails'),
    path('blog/', views.blog,name='blog'),
	path('abut/', views.abut,name='abut'),
	path('us/', views.us,name='us'),
 
]