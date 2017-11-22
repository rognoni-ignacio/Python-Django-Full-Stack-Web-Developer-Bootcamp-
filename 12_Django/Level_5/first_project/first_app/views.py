from django.shortcuts import render
from first_app.forms import UserForm, UserProfileInfoForm
# Create your views here.


def index(request):
    return render(request, 'first_app/index.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # SAVE USER
            user = user_form.save()
            # HASH PASSWORD
            user.set_password(user.password)
            # SAVE CHANGES FOR HASHED PASSWORD
            user.save(0)

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
