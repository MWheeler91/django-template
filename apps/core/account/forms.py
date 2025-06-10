from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User
from utils.common import catch_errors

class CreateUserForm(UserCreationForm):

    confirm_email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'confirm_email', 'password1', 'password2', 'first_name', 'last_name']

    catch_errors("account")
    def clean(self):
        super(CreateUserForm, self).clean()
        email = self.cleaned_data.get('email')
        confirm_email = self.cleaned_data.get('confirm_email')
        if email != confirm_email:
            # raise ValidationError('Email does not match!')
            self._errors['email'] = self.error_class(['Email does not match!'])
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            self._errors['email'] = self.error_class(["Email is already associated with an account!"])

        return self.cleaned_data
