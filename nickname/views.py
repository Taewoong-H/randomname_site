from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from .models import Animal, Adjective, Color, Food, Index, Place
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
    posts = get_object_or_404(Index, pk=pk) # Index.objects.get(pk=pk)랑 비슷한 뜻
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
    elif posts.pk==3:
        start = Adjective.objects.annotate(Count('name'))
        last = Color.objects.annotate(Count('name'))
        i = random.randrange(1, len(last))
        j = random.randrange(1, len(start))
        post = start[j] , last[i]
        return render(request, 'nickname/result.html', {'post':post})
    else:
        return render(request, 'nickname/result.html', {'posts': posts})

def throw(request):
    return render(request, 'nickname/select_name.html')

def catch(request):
    message = request.GET.get('message')
    placing = Place.objects.annotate(Count('name'))
    i = random.randrange(0, len(placing))
    naming = placing[i]
    messages = message, naming
    return render(request, 'nickname/catch.html', {'messages':messages})
'''
def place_name(request):
    placing = Place.objects.annotate(Count('name'))
    i = random.randrange(1, len(placing))
    naming = placing[i]
    return render(request, 'nickname/catch.html', {'naming':naming})
'''