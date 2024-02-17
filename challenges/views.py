from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes of walk every day!',
    'march': 'Learn a new recipe each week and cook it!',
    'april': 'Practice meditation for at least 10 minutes every day!',
    'may': 'Read a book outside of your usual genre!',
    'june': 'Start a journal and write in it daily!',
    'july': 'Learn a new language for at least 15 minutes every day!',
    'august': 'Try a new hobby or activity!',
    'september': 'Exercise for at least 30 minutes every day!',
    'october': 'Cut out processed sugar from your diet!',
    'november': 'Express gratitude by writing down three things you are thankful for each day!',
    'december': None
}

# Create your views here.


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html',{
        'months': months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html',{
            'month_name': month,
            'text': challenge_text,
        })
    except:
        raise Http404()
