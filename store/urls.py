from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('new/', views.new_book, name='new_book'),
    path('repos/', views.repos, name='repos'),
]