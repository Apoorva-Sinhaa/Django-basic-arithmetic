

from django.urls import path
from appx.views import hello_world , form_view , calculate_add

urlpatterns = [
    path('hello/', hello_world),
    path('form/',form_view, name='form'),
    path('calculate/',calculate_add, name= 'calc'),
]
