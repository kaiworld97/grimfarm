from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('seller/<int:pk>', views.seller, name='seller'),
    path('detail/<int:owner_pk>/<int:drawing_pk>', views.detail, name='detail'),
    path('buy/<int:owner_pk>/<int:drawing_pk>', views.buy, name='buy'),
]
