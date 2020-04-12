from django.urls import path
from blog import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
]
