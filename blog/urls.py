from django.urls import path
from .views import *

urlpatterns = [
    path('', list_view, name="home"),
    path('<slug>', detail_view, name="detail")
]