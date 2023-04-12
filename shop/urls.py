from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_watches, name='all_watches')
]
