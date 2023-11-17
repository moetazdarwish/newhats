from django.urls import path, include
from . import views

urlpatterns = [
    path('recievingWhatsApp/', views.recievingWhatsApp, name="recievingWhatsApp"),
]
