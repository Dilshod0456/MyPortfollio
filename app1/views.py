from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .forms import *
from .models import *
import telebot

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

    def messages(messages):
        TOKEN = '<token string>'
        tb = telebot.TeleBot('5388672945:AAGH_7J0Nc1IKOQC79O_tjw05djEbP44lfA')
        # tb.send_message(chatid, message)
        tb.send_message(1330068715, 'gogo power ranger')
    # 
    # def get_queryset(self):
        # queryset1 = Loyihalar.objects.order_by('id')
        # return queryset1