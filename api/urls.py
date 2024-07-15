from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.questions),
    path("questions/<int:id>/", views.questions),
    path('choices/', views.choices),
    path("choices/<int:id>/", views.choices),
]