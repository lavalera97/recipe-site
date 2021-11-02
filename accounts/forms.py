from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    """Форма для регистрации, берется из модели аккаунта"""

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',

    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль',

    }))

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите никнейм'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
