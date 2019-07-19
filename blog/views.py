import csv, io
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Post

def post_list(request):
    return render(request, 'blog/post_list.html', {})