from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
import datetime as DT



class LetterOfResignation_form(forms.ModelForm):
    class Meta:
        model = LetterOfResignation
        fields = ['lor_date',
    'lor_employee',
    'lor_position',
    'lor_departament',
    'lor_dateOfRes',
    'lor_additionalData']





    def saveFirst(self, user_, letter_next_num_):
        new_letter = LetterOfResignation.objects.create(
        lor_date = self.cleaned_data['lor_date'],
        lor_number = str(letter_next_num_),
        lor_employee = self.cleaned_data['lor_employee'],
        lor_position = self.cleaned_data['lor_position'],
        lor_departament = self.cleaned_data['lor_departament'],
        lor_dateOfRes = self.cleaned_data['lor_dateOfRes'],
        lor_additionalData = self.cleaned_data['lor_additionalData'],
        lor_res_officer = user_
        )

        return new_letter

class OrdersOnOtherMatters_form(forms.ModelForm):
    class Meta:
        model = OrdersOnOtherMatters
        fields = [

    'oom_date',
    'oom_content']

    def saveFirst(self, user_, order_next_num_):
        new_order = OrdersOnOtherMatters.objects.create(
            oom_number = str(order_next_num_) + "-К",
            oom_date = self.cleaned_data['oom_date'],
            oom_content = self.cleaned_data['oom_content'],
            oom_res_officer = user_
        )

        return new_order

class OrdersOnVacation_form(forms.ModelForm):
    class Meta:
        model = OrdersOnVacation
        fields = ['oov_date',
    'oov_empList']

    def saveFirst(self, user_, order_next_num_):
        new_order = OrdersOnVacation.objects.create(
            oov_number = str(order_next_num_) + "К-ОТП",
            oov_date = self.cleaned_data['oov_date'],
            oov_empList = self.cleaned_data['oov_empList'],
            oov_res_officer = user_
        )

        return new_order

class OrdersOfBTrip_form(forms.ModelForm):
    class Meta:
        model = OrdersOfBTrip
        fields = [
    'bt_date',
    'bt_place',
    'bt_dep',
    'bt_dur_from',
    'bt_dur_to',
    'bt_emloyer'
    ]

    def saveFirst(self, user_, order_next_num_, trip_dur):
        new_order = OrdersOfBTrip.objects.create(
            bt_date  = self.cleaned_data['bt_date'],
            bt_number  = str(order_next_num_) + "П",
            bt_dep = self.cleaned_data['bt_dep'],
            bt_place = self.cleaned_data['bt_place'],
            bt_emloyer = self.cleaned_data['bt_emloyer'],
            bt_dur_from = self.cleaned_data['bt_dur_from'],
            bt_dur_to = self.cleaned_data['bt_dur_to'],
            bt_res_officer = user_
        )

        return new_order


class OrdersOnPersonnel_form(forms.ModelForm):
    class Meta:
        model = OrdersOnPersonnel
        fields = [
    'op_date',
    'op_dep',
    'op_emloyer',
    'op_content']

    def saveFirst(self, user_, order_next_num_):
        new_order = OrdersOnPersonnel.objects.create(
            op_date  = self.cleaned_data['op_date'],
            op_number  = str(order_next_num_)+"ЛС",
            op_dep = self.cleaned_data['op_dep'],
            op_content = self.cleaned_data['op_content'],
            op_emloyer = self.cleaned_data['op_emloyer'],
            op_res_officer = user_
        )

        return new_order



class OutBoundDocument_form(forms.ModelForm):
    class Meta:
        model = OutBoundDocument
        fields = ['doc_type',
    'doc_date',
    'doc_dest',
    'doc_additionalData']

    def saveFirst(self, user_, doc_next_num_):
        new_document = OutBoundDocument.objects.create(
        doc_type = self.cleaned_data['doc_type'],
        doc_number = str(doc_next_num_),
        doc_date = self.cleaned_data['doc_date'],
        doc_dest = self.cleaned_data['doc_dest'],
        doc_additionalData = self.cleaned_data['doc_additionalData'],
        doc_res_officer = user_
        )

        return new_document

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'lform-input loginField', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'lform-input pwdField',
            'placeholder': '',
            'id': 'hi',
        }
))

class LetterOfInvite_form(forms.ModelForm):
    class Meta:
        model = LetterOfInvite
        fields = [ 'loi_date',
    'loi_employee',
    'loi_position',
    'loi_department',
    'loi_dateOfInv',
    'loi_additionalData']





    def saveFirst(self, user_, letter_next_num_):
        new_letter = LetterOfInvite.objects.create(
        loi_date = self.cleaned_data['loi_date'],
        loi_number = str(letter_next_num_),
        loi_employee = self.cleaned_data['loi_employee'],
        loi_position = self.cleaned_data['loi_position'],
        loi_department = self.cleaned_data['loi_department'],
        loi_dateOfInv = self.cleaned_data['loi_dateOfInv'],
        loi_additionalData = self.cleaned_data['loi_additionalData'],
        loi_res_officer = user_
        )

        return new_letter

class LaborContract_form(forms.ModelForm):
    class Meta:
        model = LaborContract
        fields = [
    'lc_date',
    'lc_dateOfInv',
    'lc_emloyer',
    'lc_pos',
    'lc_dep',
    'lc_workCond']

    def saveFirst(self, user_, order_next_num_, year_):
        new_contract = LaborContract.objects.create(
            lc_date  = self.cleaned_data['lc_date'],
            lc_number  = str(order_next_num_)+"("+str(year_)+")",
            lc_pos  = self.cleaned_data['lc_pos'],
            lc_dep = self.cleaned_data['lc_dep'],
            lc_dateOfInv = self.cleaned_data['lc_dateOfInv'],
            lc_workCond = self.cleaned_data['lc_workCond'],
            lc_emloyer = self.cleaned_data['lc_emloyer'],
            lc_res_officer = user_
        )

        return new_contract

class EmploymentHistory_form(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = [
            'eh_number',
            'eh_dateOfInv',
            'eh_employer',
            'eh_pos',
            'eh_dep',
            'eh_OrderInv',
            'eh_OrderResign',
            'eh_dateOfResign']

    def saveFirst(self, user_):
        new_empHistory = EmploymentHistory.objects.create(
            eh_number = self.cleaned_data['eh_number'],
            eh_dateOfInv = self.cleaned_data['eh_dateOfInv'],
            eh_employer = self.cleaned_data['eh_employer'],
            eh_pos = self.cleaned_data['eh_pos'],
            eh_dep = self.cleaned_data['eh_dep'],
            eh_OrderInv = self.cleaned_data['eh_OrderInv'],
            eh_OrderResign = self.cleaned_data['eh_OrderResign'],
            eh_dateOfResign = self.cleaned_data['eh_dateOfResign'],
            eh_res_officer = user_ )

        return new_empHistory
