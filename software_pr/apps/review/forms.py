from django import forms
from django.core.exceptions import ValidationError
import re
from review.models import Review
import dbl
# Импорт общего приложения 
import util.forms

# Форма для добавления отзыва
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         # Описание используемой модели и полей на форме, а также их атрибутов
#         model = Review
#         fields = ['content', 'comment', 'email_phone', 'name', 'star', 'software']
 
#         widgets = {
#             'name': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'name'}),
#             'email_phone': forms.TextInput(attrs={'required':True, 'id' : 'ephone', 'maxlength' : 25}),
#             'content': forms.Textarea(attrs={'rows':5, 'id' : 'content'}),
#             'comment': forms.Textarea(attrs={'rows':5, 'id' : 'comment'}),
#             'star': forms.TextInput(attrs={'required':True,'type':'radio'}),
            
#         }
#         # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
#         # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...




# Форма элементов для поиска заказов
class ReviewForm(forms.Form):

    name = forms.CharField(required=False, max_length=100)
    email_phone = forms.CharField(max_length=50)
    content = forms.CharField(required=False)
    # image = forms.ImageField(required=False)
    star = forms.CharField()
    file = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))



    #  Ф-ии проверки валидности полей
    def clean_name(self):

        if self.cleaned_data['name'] is not None and str(self.cleaned_data['name']) != "":

            return util.forms.clean_name(self)

    def clean_email_phone(self):

        return util.forms.clean_email_phone(self)

    def clean_star(self):
        star = self.cleaned_data['star']
        dbl.log('звезда !'+str(star))
        # Проверка валидности значения рейтинга
        if star == "":
            dbl.log('звездыыыыы'+str(star))
            raise ValidationError("Пожалуйста поставьте оценку")

        return star



# # Форма для добавления отзыва
# class ReviewForm(forms.Form):
#     # class Meta:
#     #     # Описание используемой модели и полей на форме, а также их атрибутов
#     #     model = Review
#     #     fields = ['content', 'comment', 'email_phone', 'name', 'star', 'software', 'file']
 
#     #     widgets = {
#     #         'name': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'name'}),
#     #         'email_phone': forms.TextInput(attrs={'required':True, 'id' : 'ephone', 'maxlength' : 25}),
#     #         'content': forms.Textarea(attrs={'rows':5, 'id' : 'content'}),
#     #         'comment': forms.Textarea(attrs={'rows':5, 'id' : 'comment'}),
#     #         'star': forms.TextInput(attrs={'required':True,'type':'radio'}),
#     #         'file': forms.TextInput(attrs={'required':False,'type':'file'}),
            
#     #     }
#     #     # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
#     #     # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...

#     content = forms.CharField( required=False)
#     comment = forms.CharField(required=False)
#     name = forms.CharField(required=False)
#     email_phone = forms.CharField()
#     star = forms.CharField()
#     file = forms.CharField(required=False)



    # #  Ф-ии проверки валидности полей
    # def clean_name(self):

    #     if self.cleaned_data['name'] is not None:

    #         return util.forms.clean_name(self)

    # def clean_email_phone(self):

    #     return util.forms.clean_email_phone(self)

    # def clean_star(self):
    #     star = self.cleaned_data['star']
    #     dbl.log('звезда !'+str(star))
    #     # Проверка валидности значения рейтинга
    #     if star == "":
    #         dbl.log('звездыыыыы'+str(star))
    #         raise ValidationError("Пожалуйста поставьте оценку")

    #     return star













# Форма элементов для поиска отзывов
class Search_ReviewForm(forms.Form):

    rating_from = forms.CharField(max_length=5, required=False)
    rating_to = forms.CharField(max_length=5, required=False)
    date_from = forms.DateField(required=False)
    date_to = forms.DateField(required=False)
    review_type = forms.CharField(required=False)
    count = forms.CharField(required=False)
    page = forms.CharField(required=False)
    sort = forms.CharField(required=False)

    #  Ф-ии проверки валидности полей
    def clean_date_from(self):
        
        date_from = self.cleaned_data['date_from']
        dbl.log('звездыыыыы'+str(date_from))
        if date_from is not None:

            return util.forms.clean_date(date_from)
