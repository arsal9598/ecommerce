from django.urls import path
from . import views

urlpatterns = [
    path('charge/', views.charge, name='charge'),
    path('', views.ProductListView.as_view(), name='products'),
]
