from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Place


class PlaceCreate(CreateView):
  model = Place
  fields = ['address']
  success_url = '/places/index/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['mapbox_access_token'] = 'pk.eyJ1IjoibGFyZ2V3YXRlciIsImEiOiJjbDZoOTAwZWkweWNjM2JvYThnbm03YjMzIn0.r11MoNzvczr0RUCDmi9brQ'
    context['place'] = Place.objects.all()
    return context

class PlaceList(ListView):
  model = Place
  template_name = 'places/list.html'
  context_object_name = 'places'
  paginate_by = 5

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def index(request):
  places = Place.objects.all()
  return render(request, 'places/index.html', { 'places': places })


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
