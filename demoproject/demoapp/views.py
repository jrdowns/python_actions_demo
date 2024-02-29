from django.shortcuts import render
from django.http import HttpResponse

def polo_view(request):
    return HttpResponse("Polo")