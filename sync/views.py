from django.http import HttpResponse
from django.shortcuts import render
from models import Group, Run


def index(request):
    groups = Group.objects.all()
    runs = Run.objects.all()
    return render(request, 'index.html', {'groups': groups, 'runs': runs})
