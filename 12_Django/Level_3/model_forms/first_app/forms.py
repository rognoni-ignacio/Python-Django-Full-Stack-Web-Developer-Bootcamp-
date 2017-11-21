from django.forms import ModelForm
from django.core import validators
from first_app.models import User


class UserForm(ModelForm):
    # CUSTOM VALIDATORS GO HERE
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'email']
