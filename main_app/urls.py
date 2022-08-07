from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('places/index/', views.index, name='index'),
  path('places/new/', views.PlaceCreate.as_view(), name='places_create'),
  path('places/list/', views.PlaceList.as_view(), name='places_list'),
]