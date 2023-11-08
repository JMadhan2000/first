from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jampandu(request):
    return HttpResponse('<h1><marquee>Hii how are you</h1></marquee>')

def jigelrani(request):
    return HttpResponse('<h1><marquee>i am fine and u</h1></marquee>')
