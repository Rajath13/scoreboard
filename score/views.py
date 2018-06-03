from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Scores

# Create your views here.
# def index(request):
#     return render(request,'score/index.html')
class ScoresCreate(CreateView):
    """ View for the form on Scores Model"""
    model = Scores
    fields = ['Abhinav', 'Harshith', 'Rajath', 'Winner', 'deal']

def results(request):
    """ Results view"""
    return render(request, 'score/results.html')
