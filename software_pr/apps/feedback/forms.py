# from django import forms
# from django.core.exceptions import ValidationError
# from feedback.models import *
# import re
# import dbl

from django import forms
from django.core.exceptions import ValidationError
import re
from feedback.models import Feedback
# from util.forms import clean_name
import dbl
import util.forms
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'phone', 'name']

        widgets = {
            'comment': forms.Textarea(attrs={}),
            'phone': forms.TextInput(attrs={'required':True}),
            'name': forms.TextInput(attrs={}),
        }

        # def clean_phone(self):
        #     email = self.cleaned_data['phone']
        #     if User.objects.filter(email=email).exists():
        #         raise ValidationError("Email already exists")
        #     return email

    def clean_name(self):

        if self.cleaned_data['name'] is not None:

            dbl.log("1111 !!!!")
            return util.forms.clean_name(self)

    def clean_phone(self):

        dbl.log("тел")
        # return clean_name(self)

        # dbl.log("1111 !!!!")
        return util.forms.clean_phone(self)


