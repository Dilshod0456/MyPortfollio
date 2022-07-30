from .models import Loyihalar

def extra(request):
    loyihalar = Loyihalar.objects.all
    return {'Loyihalar' : loyihalar}