# from django.shortcuts import render

from django.http import HttpResponse


def blog(request):
    return HttpResponse('Página blog')

def comment(request):
    return HttpResponse('Comentário cativante')
