from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_watches, name='shop'),
    path('watch/<watch_id>', views.watch_detail, name='watch_detail'),
]
