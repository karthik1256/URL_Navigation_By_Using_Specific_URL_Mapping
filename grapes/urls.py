from grapes.views import *
from django.urls import path

app_name='list'

urlpatterns=[
    path('pandu/',pandu,name='pandu')
]