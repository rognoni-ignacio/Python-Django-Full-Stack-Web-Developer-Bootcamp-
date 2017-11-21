from django import forms
from django.core import validators

# ONLY FOR INDIVIDUAL VALIDATIONS
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with z')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False,
                                  widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        verify_email = all_cleaned_data['verify_email']
        if email != verify_email:
            raise forms.ValidationError("Emails don't match")

            
    # THIS IS NOT COMMON. DJANGO VALIDATORS ARE USED INSTEAD
    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("The bot was catched")
    #     return bot_catcher
