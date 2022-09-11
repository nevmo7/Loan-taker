from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getBalanceSheet', views.getBalanceSheet, name='getBalanceSheet'),
    path('getLoanApproval', views.getLoanApproval, name='getLoanApproval'),
]