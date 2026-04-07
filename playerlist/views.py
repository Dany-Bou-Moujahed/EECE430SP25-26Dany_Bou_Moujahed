from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Player
from .forms import PlayerForm

class PlayerListView(ListView):
    model =Player
    template_name="playerlist/player_list.html"
    context_object_name="playerlist"

class PlayerDetailView(DetailView):
    model = Player
    template_name= "playerlist/player_detail.html"

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name= "playerlist/player_form.html"
    success_url = reverse_lazy("playerlist:list")

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = "playerlist/player_form.html"
    success_url =reverse_lazy("playerlist:list")

class PlayerDeleteView(DeleteView):
    model = Player
    template_name= "playerlist/player_confirm_delete.html"
    success_url = reverse_lazy("playerlist:list")

# Create your views here.
