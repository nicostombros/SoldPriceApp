from react import views
from django.urls import path

urlpatterns = [
    path('app/', views.home, name='home')
]
