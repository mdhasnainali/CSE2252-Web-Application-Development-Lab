from django.urls import path
from . import views

urlpatterns = [
    path('dogs/', views.DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name='dog-detail'),
    path('breeds/', views.BreedList.as_view(), name='breed-list'),
    path('breeds/<str:pk>/', views.BreedDetail.as_view(), name='breed-detail'),
]