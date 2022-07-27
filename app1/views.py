from time import time
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import *
# Create your views here.
class HomeView(CreateView):
    template_name = 'home.html'
    context_object_name = "Loyihalar"
    def get_queryset(self):
        queryset1 = Loyihalar.objects.order_by('id')