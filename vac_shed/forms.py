from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
import datetime as DT
from reg_jounals.models import logs, logs_event

from TURV.models import Department

class Vacshed_form(forms.Form):
    year = forms.CharField(label="Год (ТОЛЬКО 4 ЦИФРЫ!)", widget=forms.NumberInput(attrs={'maxlength':'4'}))
    dep = forms.ModelChoiceField(label='Подразделение', queryset=Department.objects.none(), required=True)

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', 'all')

        super(Vacshed_form, self).__init__(*args, **kwargs)
        print('USER: ' + str(user_id))
        if user_id != 'all':
            self.fields['dep'].queryset = Department.objects.filter(user=user_id)
        else:
            self.fields['dep'].queryset = Department.objects.all()

    def saveFirst(self, user_):

        next_id = int(VacantionShedule.objects.latest('id').id) + 1
        logs.objects.create(
            date = DT.datetime.now(),
            event = logs_event.objects.get(id=3),
            doc_id = next_id,
            type = 'График отпусков',
            number = next_id,
            year = self.cleaned_data['year'],
            doc_date = DT.datetime.strptime(str(self.cleaned_data['year'] + '-' + str(DT.datetime.now().month) + '-' + str(DT.datetime.now().day)), '%Y-%M-%d'),
            addData = 'График отпусков: ' + str(self.cleaned_data['dep'].name) + ' за: ' + str(self.cleaned_data['year']) + ' год',
            link = '/vacshed/create/' + str(next_id) + '/',
            res_officer = user_)

        new_vacshed = VacantionShedule.objects.create(
            year = self.cleaned_data['year'],
            dep = self.cleaned_data['dep'],
            res_officer = user_)

        return new_vacshed
