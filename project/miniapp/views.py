from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def models_list(request):
    random_number = random.randint(1, 6)
    return HttpResponse(f"{random_number}")

def post_list(request):
    a = random.randint(1, 6)
    return render(request, 'miniapp/post_list.html', {"promena" : a})
