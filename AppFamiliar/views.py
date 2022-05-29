from django.shortcuts import render
from .models import Familiar

# Create your views here.
def familiar(request):
    familiares_list = Familiar.objects.all()
    return render(request, 'familiares.html',{'familiares':familiares_list})