from django import forms
from django.db import models
from .models import BurnoutSurvey

class BurnoutSurveyForm(forms.ModelForm):
    class Meta:
        model = BurnoutSurvey
        fields = '__all__'
        widgets = {
            field.name: forms.RadioSelect(attrs={'class': 'custom-radio'}) 
            for field in BurnoutSurvey._meta.get_fields() 
            if isinstance(field, models.IntegerField)
        }

    def __init__(self, *args, **kwargs):
        super(BurnoutSurveyForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.empty_label = None
            field.choices = BurnoutSurvey.STATEMENT_CHOICES
            field.required = True
