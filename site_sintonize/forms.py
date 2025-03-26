from django import forms
from django.db import models
from .models import BurnoutSurvey

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
