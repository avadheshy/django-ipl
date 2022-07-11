from unittest import result
from django.shortcuts import render
from match.models import Matches, Deliveries
from django.db.models import Count, Sum

# Create your views here.


def index(request):
    return render(request, 'index.html')


def played(request):
    result = Matches.objects.values('season').annotate(
        play=Count('id')).order_by('season')
    return render(request, 'played.html', {'res': result})


def won(request):
    result=Matches.objects.values('season', 'winner').annotate(win=Count('winner')).order_by('season', 'winner')

    return render(request, 'won.html', {'res': result})


def runs(request):
    result = Deliveries.objects.filter(match__season=2016).values(
        'bowling_team').annotate(extras=Sum('extra_runs')).order_by('extras')
    return render(request, 'runs.html', {'res': result})


def bowler(request):
    result = Deliveries.objects.filter(match__season=2015).values('bowler').annotate(
        economy=Sum('total_runs')*6/Count('id')).order_by('economy')[0:10]
    return render(request, 'bowler.html', {'res': result})
