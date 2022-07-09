from django.shortcuts import render
from match.models import Matches,Deliveries
from django.db.models import Count,Sum

# Create your views here.
def index(request):
    return render(request,'index.html')
def played(request):
    result=Matches.objects.values('team1').annotate(win=Count('id'))
    return render(request,'played.html',{'res':result})
def won(request):
    result=Matches.objects.values('season','winner').order_by('season').annotate(win=Count('winner'))
    return render(request,'won.html',{'res':result})
def runs(request):
    result=Matches.objects.values(season=2015).select_related(
        Deliveries.objects.values('bowling_team',
    'extra_runs').annotate(Sum('extra_runs')))
    return render(request,'runs.html',{'res':result})


def bowler(request):
    result=Matches.objects.values_list('id').filter(season=2015)
    return render(request,'bowler.html',{'res':result})
    
