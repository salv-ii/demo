from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('add/',views.addition,name='addition'),
    path('contact/',views.contact,name='contact'),
    path('details/',views.details,name='details'),
    path('thanku/',views.thanku,name='thnx')
]