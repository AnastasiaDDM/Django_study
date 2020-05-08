from django import forms
# from django.core.exceptions import ValidationError
from feedback.models import *

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'phone', 'name']

        widgets = {
            'comment': forms.Textarea(attrs={}),
            'phone': forms.TextInput(attrs={'required':True}),
            'name': forms.TextInput(attrs={}),
        }


