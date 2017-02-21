from django.http import HttpResponse
from django.shortcuts import render
from models import Group

__author__ = 'kenneth'


def index(request):
    groups = Group.objects.all()
    return render(request, 'index.html', {'groups': groups})
