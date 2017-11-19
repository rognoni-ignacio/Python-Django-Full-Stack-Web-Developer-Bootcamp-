from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")


def help(request):
    my_dict = {"help_text": "This is the help page!"}
    return render(request, 'second_app/help.html', context=my_dict)