from django import forms

class OutBoundDocument_form(forms.Form):
    doc_type = forms.CharField(max_length=100, help_text="Введите вид документа (письмо, справка, и.т.д)")
    doc_date = forms.DateField(help_text="Введите дату документа", input_formats=[''%d.%m.%Y'])
