from django.urls import path
from .views import *
app_name = 'app1'

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
]
