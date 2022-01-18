from xml.dom.pulldom import CHARACTERS
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'amma@@1953'})

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    else: pass
    
    if request.GET.get('special'):
        characters.extend(list('!@#$&'))
    else: pass
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    else: pass
    
    length = int(request.GET.get('length'))
    
    the_password = ''
    for x in range(length):
        the_password+=random.choice(characters)
    
    
    return render(request, 'generator/password.html', {'password': the_password})

def abtme(request):
    return render(request, 'generator/about.html', {})