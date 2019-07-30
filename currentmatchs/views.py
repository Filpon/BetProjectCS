import csv, io
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Cesvcurrentmatchs
from .forms import CesvcurrentmatchsForm
from django.http import HttpResponse
from currentmatchs.topteams import top_teams_left, top_teams_right
from django.core.paginator import Paginator

def tablecurrentmatchs(request):
    cesvpresent = Cesvcurrentmatchs.objects.all()
    return render(request, 'currentmatchstable.html', {'cesvpresent': cesvpresent, 'top_teams_left': top_teams_left, 'top_teams_right': top_teams_right})

def currentmatchsget(request):
    template = 'currentmatchsform.html'

    if request.method == "POST":
        form = CesvcurrentmatchsForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = CesvcurrentmatchsForm()
    
    context = {
        'form': form,
    }
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def Cesvcurrentmatchs_upload(request):
    template = "Cesvcurrentmatchs_upload.html"
    
    prompt = {
        'order': 'Left_team_title; Left_team_coefficients; Moneybet_for_left_team; Left_team_win_percent; Time_before_match;Right_team_title; Right_team_coefficients; Right_team_win_percent; Moneybet_for_right_team' 
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
        _, created = Cesvcurrentmatchs.objects.update_or_create(
            Left_team_title = column[0],
            Left_team_coefficients = column[1],
            Moneybet_for_left_team = column[2],
            Left_team_win_percent = column[3],
            Time_before_match = column[4],
            Right_team_title = column[5],
            Right_team_coefficients = column[6],
            Moneybet_for_right_team = column[7],
            Right_team_win_percent = column[8]
        )

    context = {}
    return render(request, template, context)
# Create your views here.