from django.urls import path
from . import views

urlpatterns =[
    path('<str:pk>/',views.func1,name='api')
]