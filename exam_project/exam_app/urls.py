from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='exam_app'),
    path('films/', views.film_rating, name='film_rating'),
]
