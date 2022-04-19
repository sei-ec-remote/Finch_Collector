# main_app/views.py
from django.shortcuts import render

from main_app.models import Pizza



def index(request):
    # render index.html
    return render(request, 'index.html')


def about(request):
    # render about page
    return render(request, 'about.html')


# class Pizza:
#     def __init__(self, name, type, toppings):
#         self.name = name
#         self.type = type
#         self.toppings = toppings

# pizzas = [
#     Pizza('Chicago', 'deep-dish', ['cheese','tomato sauce','extra tomato sauce']),
#     Pizza('Neapolitan', 'hand toss', ['tomato sauce','mozzarella','fresh basil','olive oil']),
#     Pizza('Meatza', 'hand toss', ['pepperoni','sausage','meatball','bacon','ham','tomato sauce','cheese'])
# ]

def pizza_index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza/index.html',{'pizzas':pizzas})

def pizza_show(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    return render(request, 'pizza/show.html', {'pizza':pizza})