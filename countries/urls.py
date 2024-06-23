from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.countries_list, name='countries_list'),
    path('countries/<int:pk>/', views.countries_detail, name='countries_detail'),
]

