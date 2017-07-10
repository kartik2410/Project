from django.shortcuts import render
from .models import Gift

# Create your views here.

def Home(request):
    gift = Gift.objects.get(GiftId=1)
    return render(request, 'project1/home.html', {'gifts' : gift})

def Blog(request):
    return render(request, 'project1/blog.html', )

def Art(request):
    return render(request, 'project1/art.html', )

def Gifts(request):
    gifts = Gift.objects.all()
    return render(request, 'project1/gifts.html', {'gifts' : gifts} )

def Cakes(request):
    return render(request, 'project1/cakes.html', )
