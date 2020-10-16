from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class OutBoundDocument_form(forms.Form):
    doc_type = forms.CharField(label='Вид документа',max_length=100, help_text="Введите вид документа (письмо, справка, и.т.д)")
    doc_date = forms.DateField(label='Дата документа',help_text="Введите дату документа", input_formats=['%d.%M.%Y'])
    doc_dest = forms.CharField(label='Адресат',max_length=256, help_text="Введите адресата")
    doc_additionalData = forms.CharField(label='Содержание', help_text="Введите содержание",widget=forms.Textarea)
    doc_res_officer = forms.CharField(max_length=256, required = False, help_text="Сотрудник, который внес документ в систему")

    def save(self):
        new_document = OutBoundDocument.objects.create(
            doc_type = self.cleaned_data['doc_type'],
            doc_date = self.cleaned_data['doc_date'],
            doc_dest = self.cleaned_data['doc_dest'],
            doc_additionalData = self.cleaned_data['doc_additionalData'],
            doc_res_officer = self.cleaned_data['doc_res_officer']
            )
        return new_document

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'lform-input', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'lform-input',
            'placeholder': '',
            'id': 'hi',
        }
))
