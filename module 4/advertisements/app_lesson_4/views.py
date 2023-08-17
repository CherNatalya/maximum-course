from django.shortcuts import render
from django.http import HttpResponse


def less4(request):
    return HttpResponse('Домашка по 4 занятию')
