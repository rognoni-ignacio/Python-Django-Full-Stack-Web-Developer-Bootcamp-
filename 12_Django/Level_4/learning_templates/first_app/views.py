from django.shortcuts import render

# Create your views here.


def index(request):
    my_dictionary = {'text': 'hello world', 'integer': 100}
    return render(request, 'first_app/index.html', context=my_dictionary)


def other(request):
    return render(request, 'first_app/other.html')


def relative(request):
    return render(request, 'first_app/relative-url-templates.html')
