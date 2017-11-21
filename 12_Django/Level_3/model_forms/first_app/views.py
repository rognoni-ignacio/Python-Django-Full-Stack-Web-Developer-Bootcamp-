from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User
from first_app.forms import UserForm
# Create your views here.


def index(request):
    users_list = User.objects.all()
    my_dict = {'users_list': users_list}
    return render(request, 'first_app/index.html', context=my_dict)


def users(request):
    users_list = User.objects.all()
    my_dict = {'users_list': users_list}
    return render(request, 'first_app/index.html', context=my_dict)


def user_form_view(request):
    users_list = User.objects.all()
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            print("Validation success")
            print("First Name: " + user_form.cleaned_data['first_name'])
            print("Last Name: " + user_form.cleaned_data['last_name'])
            print("Email: " + user_form.cleaned_data['email'])
            user_form.save()
            user_form = UserForm()
        else:
            print("ERROR: Form invalid")

    return render(request, 'first_app/index.html', {'form': user_form, 'users_list': users_list})
