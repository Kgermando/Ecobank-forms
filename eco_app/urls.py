from django.urls import path

from eco_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addForm, name='add'),
]
