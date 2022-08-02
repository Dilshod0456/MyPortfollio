from django.shortcuts import redirect, reverse, render
from django.views.generic import CreateView
from .forms import *
from .models import *
from .sent_message import *

class HomeView(CreateView):
    template_name = 'home.html'
    form_class = XabarCreatForm
    model = Xabarlar

    def form_valid(self ,form):
        Xabar = form.save(commit=False)
        Xabar.save()

        m_message = send_message(
                message_tg.format(
                    Xabar.fish,
                    Xabar.email,
                    Xabar.tell,
                    Xabar.text,
                )
            )
        return redirect('app1:Home')
    