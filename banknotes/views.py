from django.shortcuts import render
# from .models import Banknote
from django.http import HttpResponse

# Create your views here.
def index(request):
    # banknotes = Banknote.objects.all()
    # return render(request, 'banknotes/index.html', {'banknotes': banknotes})

    return HttpResponse("Hello, world. You're at the polls index.")