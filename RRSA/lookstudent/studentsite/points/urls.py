from django.urls import path

from . import views

urlpatterns = [
    #build a url pattern to take id as a score
    path('<str:id>', views.index, name='index'),
]