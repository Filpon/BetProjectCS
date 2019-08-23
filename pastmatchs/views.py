import csv, io
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import CesvPastMatchs
from .forms import CesvPastMatchsForm
from django.http import HttpResponse
# from django_tables2 import SingleTableView

# class PeopleListView(SingleTableView):
#     table = PeopleTable

def TablePastMatchs(request):
    cesvpast = CesvPastMatchs.objects.all()
    context = {'cesvpast': cesvpast}
    # Создаём Paginator, в который передаём элементы таблицы и указываем, что их будет 10 штук на одну страницу
    current_page = Paginator(cesvpast, 10)
    # Pagination в django_bootstrap3 посылает запрос вот в таком виде:
    # "GET /?page=2 HTTP/1.0" 200,
    # Поэтому нужно забрать page и попытаться передать его в Paginator для нахождения страницы
    page = request.GET.get('page')
    try:
        # Если существует, то выбираем эту страницу
        context['cesvpastmatchs_lists'] = current_page.page(page)  
    except PageNotAnInteger:
        # Если None, то выбираем первую страницу
        context['cesvpastmatchs_lists'] = current_page.page(1)  
    except EmptyPage:
        # Если вышли за последнюю страницу, то возвращаем последнюю
        context['cesvpastmatchs_lists'] = current_page.page(current_page.num_pages)
    # django_tables2.RequestConfig(request, paginate={'per_page': 25}).configure(cesvpast)
    return render(request, 'outputtableh.html', context)

def PastMatchsGet(request):
    template = 'pastmatchs.html'

    if request.method == "POST":
        form = CesvPastMatchsForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = CesvPastMatchsForm()
    
    context = {
        'form': form,
    }
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def CesvPastMatchs_upload(request):
    template = "Cesvpastmatchs_upload.html"
    
    prompt = {
        'order': 'Order should be: left team title, moneybet for left team, score, right team title, moneybet for right team, winning team/match result, hypothesis' 
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
        _, created = CesvPastMatchs.objects.update_or_create(
            left_team_title = column[0],
            moneybet_for_left_team = column[1],
            score = column[2],
            right_team_title = column[3],
            moneybet_for_right_team = column[4],
            winning_team_match_result = column[5],
            hypothesis = column[6]
        )

    context = {}
    return render(request, template, context)
