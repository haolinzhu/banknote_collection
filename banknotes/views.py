from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Banknote


# Create your views here.
def index(request):
    country_list = Banknote.objects.values_list('country', flat=True).distinct().order_by('country')
    template = loader.get_template('banknotes/index.html')
    context = {
        'country_list': country_list,
    }
    return HttpResponse(template.render(context, request))


def banknotes(request, country):
    return HttpResponse("You're looking at banknotes of %s." % country)
