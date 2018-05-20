from django.shortcuts import render

# Create your views here.
from . import forms

def game_list(request):
	search_form = forms.SearchForm()
	return render(request, "gameViewer/game_list.html", {"search_form": search_form})

def game_detail(request, pk):
	return render(request, "gameViewer/game_detail.html")

def game_view_test(request):
	return render(request, "gameViewer/display_game.html")