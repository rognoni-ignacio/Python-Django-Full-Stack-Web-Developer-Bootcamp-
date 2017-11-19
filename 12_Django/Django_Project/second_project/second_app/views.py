from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
# Create your views here.


def index(request):
    return HttpResponse("<em>My Second App</em>")


def help(request):
    my_dict = {"help_text": "This is the help page!"}
    return render(request, 'second_app/help.html', context=my_dict)


def users(request):
    users_list = User.objects.all()
    my_dict = {'users_list': users_list}
    return render(request, 'second_app/index.html', context=my_dict)
