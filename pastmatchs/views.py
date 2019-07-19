import csv, io
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Cesvpastmatchs
from .forms import CesvpastmatchsForm
from django.http import HttpResponse

def tablepastmatchs(request):
    cesvpast = Cesvpastmatchs.objects.all()
    return render(request, 'outputtableh.html', {'cesvpast': cesvpast})

def pastmatchsget(request):
    template = 'pastmatchs.html'

    if request.method == "POST":
        form = CesvpastmatchsForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = CesvpastmatchsForm()
    
    context = {
        'form': form,
    }
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def Cesvpastmatchs_upload(request):
    template = "Cesvpastmatchs_upload.html"
    
    prompt = {
        'order': 'Order should be: Left team title, Moneybet for left team, Score, Right team title, Moneybet for right team, Winning team/match result, Hypothesis' 
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
        _, created = Cesvpastmatchs.objects.update_or_create(
            Left_team_title = column[0],
            Moneybet_for_left_team = column[1],
            Score = column[2],
            Right_team_title = column[3],
            Moneybet_for_right_team = column[4],
            Winning_team_match_result = column[5],
            Hypothesis = column[6]
        )

    context = {}
    return render(request, template, context)