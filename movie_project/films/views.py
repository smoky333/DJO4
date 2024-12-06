from django.shortcuts import render, redirect, get_object_or_404
from .models import Film
from .forms import FilmForm

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

def delete_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        film.delete()
        return redirect('film_list')
    return render(request, 'films/delete_film.html', {'film': film})
from django.shortcuts import render

# Create your views here.
