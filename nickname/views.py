from django.shortcuts import render
from django.db.models import Count
from .models import Animal, Adjective, Food
import random

# Create your views here.
def select_name(request):
    start = Adjective.objects.annotate(Count('name'))
    last = Food.objects.annotate(Count('name'))
    i = random.randrange(1, len(last))
    j = random.randrange(1, len(start))
    posts = start[j] , last[i]
    return render(request, 'nickname/select_name.html', {'posts':posts})


'''
def show_name(request):
    last = Food.objects.annotate(Count('name'))
    i = random.randrange(1, len(last))
    posts = last[i]
    return render(request, 'nicknama/show_name.html',{'posts':posts})
''' 
