"""Render module to render templates , Create View module to create a form for Scores Model"""
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.db.models import Sum, Avg
from .models import Scores

# Create your views here.
# def index(request):
#     return render(request,'score/index.html')
class ScoresCreate(CreateView):
    """ View for the form on Scores Model"""
    model = Scores
    fields = ['Session', 'Abhinav', 'Harshith', 'Rajath', 'Winner', 'deal']

def results(request):
    """ Results view"""
    all_scores = Scores.objects.all()
    game_count = Scores.objects.count()
    abhinav_avg = Scores.objects.aggregate(Avg('Abhinav'))
    harshith_avg = Scores.objects.aggregate(Avg('Harshith'))
    rajath_avg = Scores.objects.aggregate(Avg('Rajath'))
    abhinav_sum = Scores.objects.aggregate(Sum('Abhinav'))
    harshith_sum = Scores.objects.aggregate(Sum('Harshith'))
    rajath_sum = Scores.objects.aggregate(Sum('Rajath'))
    sum_date = Scores.objects.values('Date').annotate(
        Sum('Abhinav'), Sum('Harshith'), Sum('Rajath')
    )
    sum_session = Scores.objects.values('Session').annotate(
        Sum('Abhinav'), Sum('Harshith'), Sum('Rajath')
    )
    abhinav_wins = Scores.objects.filter(Winner='Abhinav').count()
    harshith_wins = Scores.objects.filter(Winner='Harshith').count()
    rajath_wins = Scores.objects.filter(Winner='Rajath').count()
    abhinav_eighties = Scores.objects.filter(Abhinav=80).count()
    harshith_eighties = Scores.objects.filter(Harshith=80).count()
    rajath_eighties = Scores.objects.filter(Rajath=80).count()
    abhinav_deals = Scores.objects.filter(deal='Y').filter(Winner='Abhinav').count()
    harshith_deals = Scores.objects.filter(deal='Y').filter(Winner='Harshith').count()
    rajath_deals = Scores.objects.filter(deal='Y').filter(Winner='Rajath').count()
    abhinav_session_win = 0
    harshith_session_win = 0
    rajath_session_win = 0

    context = {
        'all_scores':all_scores,
        'game_count' : game_count,
        'abhinav_avg' : abhinav_avg['Abhinav__avg'],
        'harshith_avg' : harshith_avg['Harshith__avg'],
        'rajath_avg' : rajath_avg['Rajath__avg'],
        'abhinav_sum' : abhinav_sum['Abhinav__sum'],
        'harshith_sum' : harshith_sum['Harshith__sum'],
        'rajath_sum' : rajath_sum['Rajath__sum'],
        'abhinav_wins': abhinav_wins,
        'harshith_wins': harshith_wins,
        'rajath_wins' : rajath_wins,
        'abhinav_eighties':abhinav_eighties,
        'harshith_eighties':harshith_eighties,
        'rajath_eighties':rajath_eighties,
        'abhinav_deals':abhinav_deals,
        'harshith_deals':harshith_deals,
        'rajath_deals':rajath_deals,
        'sum_date': sum_date,
        "sum_session" : sum_session,
        'abhinav_session_win': abhinav_session_win,
        'harshith_session_win': harshith_session_win,
        'rajath_session_win': rajath_session_win
    }
    return render(request, 'score/results.html', context=context)
