from django import forms

from .models import Apply, job

class ApllyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'cv', 'website', 'cover_letter']

class jobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('slug', 'owner',)