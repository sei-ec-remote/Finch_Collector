from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

# About page that describes the app
def about(request):
    return render(request, 'about.html')

class Movie:
    def __init__(self, name, genre, description, year):
        self.name = name,
        self.genre = genre,
        self.description = description,
        self.year = year

movies = [
    Movie('The Count of Monte Cristo', 'Adventure', "The Count of Monte Cristo' is an adaptation of the Alexander Dumas tale by the same name. Dantes, a sailor who is falsely accused of treason by his best friend Fernand, who wants Dantes' girlfriend Mercedes for himself. Dantes is imprisoned on the island prison of Chateau d'If for 13 years, where he plots revenge against those who betrayed him. With the help of another prisoner, he escapes the island and proceeds to transform himself into the wealthy Count of Monte Cristo as part of his plan to exact revenge", 2002)
]

def movies_index(request):
    return render(request, 'movies/index.html', {'movies': movies})