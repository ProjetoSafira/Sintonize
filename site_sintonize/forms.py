from django import forms
from django.db import models
from .models import BurnoutSurvey
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re

class BurnoutSurveyForm(forms.ModelForm):
    class Meta:
        model = BurnoutSurvey
        fields = '__all__'
        widgets = {
            'statement_1': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_2': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_3': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_4': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_5': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_6': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_7': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_8': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_9': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_10': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_11': forms.RadioSelect(attrs={'class': 'custom-radio'}),
            'statement_12': forms.RadioSelect(attrs={'class': 'custom-radio'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            # Remove a opção vazia/traços do início
            if hasattr(field, 'choices'):
                choices = list(field.choices)
                if choices and choices[0][1] == '---------':
                    field.choices = choices[1:]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correto@email.com',
            'id': 'email'
        })
    )
    
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha!',
            'id': 'password1'
        })
    )
    
    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            'id': 'password2'
        })
    )
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este e-mail já está cadastrado.')
        return email
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        
        # Validação de no mínimo 6 caracteres
        if len(password) < 6:
            raise ValidationError('A senha deve ter pelo menos 6 caracteres.')
        
        # Validação de pelo menos 1 caractere especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('A senha deve conter pelo menos 1 caractere especial.')
        
        # Validação de letras maiúsculas e minúsculas
        if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
            raise ValidationError('A senha deve conter letras maiúsculas e minúsculas.')
        
        return password
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError('As senhas não coincidem.')
        
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # Usa o email como username
        if commit:
            user.save()
        return user
