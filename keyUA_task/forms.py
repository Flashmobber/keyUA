from django import forms
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

    def save(self, commit=True):
        password = self.cleaned_data.pop("password")
        user = super(UserCreateForm, self).save()
        user.set_password(password)
        user.save()
        return user


class EntrySearchForm(forms.Form):
    date_start = forms.DateField(required=False, label="Date:",
                                 widget=forms.DateInput(attrs={
                                     "placeholder": "From"}),
                                 )
    date_end = forms.DateField(required=False, label="",
                               widget=forms.DateInput(attrs={
                                   "placeholder": "To"}))
