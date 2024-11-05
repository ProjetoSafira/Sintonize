from django import forms
from django.db import models
from .models import BurnoutSurvey

class BurnoutSurveyForm(forms.ModelForm):
    class Meta:
        model = BurnoutSurvey
        fields = '__all__'
        widgets = {
            field.name: forms.RadioSelect() 
            for field in BurnoutSurvey._meta.get_fields() 
            if isinstance(field, models.IntegerField)
        }



    def __init__(self, *args, **kwargs):
        super(BurnoutSurveyForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            # Garantir que não haja opção vazia
            field.empty_label = None
            # Reatribuir as opções com os rótulos correspondentes
            field.choices = BurnoutSurvey.STATEMENT_CHOICES
            field.required = True