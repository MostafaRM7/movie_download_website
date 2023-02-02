from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import Form


class RegisterForm(Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(250)
        ]
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    confirm_password = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('Password does\'nt match confirm password')


class LoginFrom(Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'formInput',
                'placeholder': 'example@exmp.com'
            }
        ),
        validators=[
            validators.EmailValidator,
            validators.MaxLengthValidator(100)
        ]

    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'formInput',
                'id': 'pass-input'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    remember_me = forms.BooleanField(
        label='Remember me',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'rememberme',
                'style': 'margin-top: 8px; margin-left: 10px'
            }
        ),
        required=False
    )
