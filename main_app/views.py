from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Place


class PlaceCreate(LoginRequiredMixin, CreateView):
  model = Place
  fields = ['address', 'description']
  success_url = '/places/map/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['mapbox_access_token'] = 'pk.eyJ1IjoibGFyZ2V3YXRlciIsImEiOiJjbDZoOTAwZWkweWNjM2JvYThnbm03YjMzIn0.r11MoNzvczr0RUCDmi9brQ'
    context['place'] = Place.objects.all()
    return context

class PlaceUpdate(LoginRequiredMixin, UpdateView):
  model = Place
  fields = ['address', 'description']
  success_url = '/places/map/'

class PlaceDelete(LoginRequiredMixin, DeleteView):
  model = Place
  success_url = '/places/map/'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def map(request):
  places = Place.objects.all()
  return render(request, 'places/map.html', { 'places': places })


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


class Home(LoginView):
  template_name = 'home.html'

def places_detail(request, place_id):
  place = Place.objects.get(id=place_id)
  return render(request, 'places/detail.html', { 'place': place })