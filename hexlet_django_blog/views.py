from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

TEAM = [
    {'name': 'Yoda', 'position': 'CEO'},
    {'name': 'Obi-Wan Kenobi', 'position': 'Senior Developer'},
    {'name': 'Anakin Skywalker', 'position': 'Junior Developer'},
    {'name': 'Jar Jar Binks', 'position': 'Trainee'},
]

def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def about(request):
    context = {'TEAM': TEAM}
    return render(request, 'about.html', context)

