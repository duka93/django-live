from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    error_css_class = 'error2'
    email = forms.EmailField(widget=forms.EmailInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if len(password1)<8:
            raise forms.ValidationError("Šifra treba da ima najmanje 8 karaktera")
        if password1.isnumeric():
            raise forms.ValidationError("Vaša šifra se nalazi medju najčešće korišćenim siframa")
        if password1.isalpha():
            raise forms.ValidationError("Vaša šifra se nalazi medju najčešće korišćenim siframa")
        if password1 != password2:
            raise forms.ValidationError("Vaše šifre se ne poklapaju")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if ' ' in username:
            raise forms.ValidationError("Unesite ispravno korisničko ime. Može da sadrži samo reči, brojeve i znakove @/./+/-/_ .")
        return username














