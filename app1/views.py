from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .forms import *
from .models import *
# Create your views here.
class HomeView(CreateView):
    template_name = 'home.html'
    form_class = XabarCreatForm
    model = Xabarlar
    context_object_name = "form"
    def get_success_url(self):
        return reverse('app1:Home')

    def form_valid(self, form):
        Xabar = form.save(commit=False)
        Xabar.save()
        return redirect('app1:Home')
    # 
    # def get_queryset(self):
        # queryset1 = Loyihalar.objects.order_by('id')
        # return queryset1