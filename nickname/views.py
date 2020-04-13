from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from .models import Animal, Adjective, Food, Index
import random

# Create your views here.
'''
def result_name(request):
    start = Adjective.objects.annotate(Count('name'))
    last = Food.objects.annotate(Count('name'))
    i = random.randrange(1, len(last))
    j = random.randrange(1, len(start))
    posts = start[j] , last[i]
    return render(request, 'nickname/result.html', {'posts':posts})
'''

def select_catagory(request):
    catagory = Index.objects.all()
    return render(request, 'nickname/select_name.html', {'catagory':catagory})


def result_name(request, pk):
    posts = get_object_or_404(Index, pk=pk)
    if posts.pk==2:
        start = Adjective.objects.annotate(Count('name'))
        last = Food.objects.annotate(Count('name'))
        i = random.randrange(1, len(last))
        j = random.randrange(1, len(start))
        post = start[j] , last[i]
        return render(request, 'nickname/result.html', {'post':post})
    elif posts.pk==1:
        start = Adjective.objects.annotate(Count('name'))
        last = Animal.objects.annotate(Count('name'))
        i = random.randrange(1, len(last))
        j = random.randrange(1, len(start))
        post = start[j] , last[i]
        return render(request, 'nickname/result.html', {'post':post})
    else:
        return render(request, 'nickname/result.html', {'posts': posts})

