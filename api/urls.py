from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.questions),
    path('choices/', views.choices),
]