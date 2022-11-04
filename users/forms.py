from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    error_css_class = 'error2'
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if len(password1)<8:
            raise forms.ValidationError("Šifra treba da ima najmanje 8 karaktera")
        if password1.isnumeric():
            raise forms.ValidationError("Vaša šifra se nalazi medju najčešće korišćenim siframa")
        if password1.isalpha():
            raise forms.ValidationError("Vaša šifra se nalazi medju najčešće korišćenim siframa")
        if password1 != password2:
            raise forms.ValidationError("Vaše šifre se ne poklapaju")
        return password2

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'














