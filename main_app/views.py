from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')
 
def index(request):
  return render(request, 'index.html')

def jewels_index(request):
    return render(request, 'jewels/index.html', {'jewels': jewels})

class Jewelry:
    def __init__(self, type, metal, description, color, year):
        self.type = type
        self.metal = metal
        self.description = description
        self.color = color
        self.year = year

jewels = [
    Jewelry('Earring', '14k Gold', 'Small .3mm', 'gold', 1929),
    Jewelry('Bracelet', 'Silver', 'Herringbone', 'silver', 1941),
    Jewelry('Necklace', '10k Gold', 'Gucci', 'rose', 1955),
    Jewelry('Ring', 'Platinum', 'Engagement', 'silver', 1909)
]