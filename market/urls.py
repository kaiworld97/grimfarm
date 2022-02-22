from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('seller/<int:pk>', views.seller, name='seller'),
    path('detail/<int:pk>', views.detail, name='detail'),
]
