from django.shortcuts import render
# Create your views here.
from . import forms
from .models import Game

def game_list(request):
	search_form = forms.SearchForm()
	games_list = Game.objects.all()
	return render(request, "gameViewer/game_list.html", {"search_form": search_form, "games": games_list})

def game_detail(request, pk):
	game = Game.objects.get(pk=pk)
	return render(request, "gameViewer/game_detail.html", {"game": game})