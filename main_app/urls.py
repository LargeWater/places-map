from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('places/map/', views.map, name='map'),
  path('places/new/', views.PlaceCreate.as_view(), name='places_create'),
  # path('places/list/', views.PlaceList.as_view(), name='places_list'),
  path('accounts/signup/', views.signup, name='signup'),
  path('places/<int:pk>/delete/', views.PlaceDelete.as_view(), name='places_delete'),
  path('places/<int:pk>/update/', views.PlaceUpdate.as_view(), name='places_update'),
  path('places/<int:place_id>/', views.places_detail, name='places_detail'),
]