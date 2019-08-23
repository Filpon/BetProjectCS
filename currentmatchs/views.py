import csv, io
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import CesvCurrentMatchs
from .forms import CesvCurrentMatchsForm
from django.http import HttpResponse
from currentmatchs.topteams import top_teams_left, top_teams_right
from django.core.paginator import Paginator

def TableCurrentMatchs(request):
    cesvpresent = CesvCurrentMatchs.objects.all()
    return render(request, 'currentmatchstable.html', {'cesvpresent': cesvpresent, 'top_teams_left': top_teams_left, 'top_teams_right': top_teams_right})

def CurrentMatchsGet(request):
    template = 'currentmatchsform.html'

    if request.method == "POST":
        form = CesvCurrentMatchsForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = CesvCurrentMatchsForm()
    
    context = {
        'form': form,
    }
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def CesvCurrentMatchs_upload(request):
    template = "Cesvcurrentmatchs_upload.html"
    
    prompt = {
        'order': 'left_team_title; left_team_coefficients; moneybet_for_left_team; left_team_win_percent; time_before_match; right_team_title; right_team_coefficients; right_team_win_percent; moneybet_for_right_team' 
    }

    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=';', quotechar="|"):
        _, created = CesvCurrentMatchs.objects.update_or_create(
            left_team_title = column[0],
            left_team_coefficients = column[1],
            moneybet_for_left_team = column[2],
            left_team_win_percent = column[3],
            time_before_match = column[4],
            right_team_title = column[5],
            right_team_coefficients = column[6],
            moneybet_for_right_team = column[7],
            right_team_win_percent = column[8]
        )

    context = {}
    return render(request, template, context)
# Create your views here.
