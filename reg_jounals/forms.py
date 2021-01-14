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





    def saveFirst(self, user_):
        letters = LetterOfResignation.objects.all()
        letters_count = len(letters)
        if letters_count == 0:
            letter_next_num_ = 1
        else:
            letter_prev_num = letters[letters_count - 1].lor_number
            letter_next_num_ = int(letter_prev_num) + 1
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись о заявлении об увольнении : ' + str(letter_next_num_) +  ' от '+ str(self.cleaned_data['lor_date']) + " увольняемый сотрудник: " + str(self.cleaned_data['lor_employee']) + '\n'  )
        log.close()
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

    def saveFirst(self, user_):
        orders = OrdersOnOtherMatters.objects.all()
        orders_count = len(orders)
        if orders_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[orders_count - 1].oom_number
            cut_symb = (len(str(order_prev_num)) - 2)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1
            log = open('log.txt', 'a')
            log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись: ' + str(order_next_num_) + "-К" + ' от '+ str(self.cleaned_data['oom_date']) + '\n'  )
            log.close()
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

    def saveFirst(self, user_):
        orders = OrdersOnVacation.objects.all()
        orders_count = len(orders)
        if orders_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[orders_count - 1].oov_number
            cut_symb = (len(str(order_prev_num)) - 5)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись: ' + str(order_next_num_ ) + 'К-ОТП '+  ' от '+ str(self.cleaned_data['oov_date'])  + '\n'  )
        log.close()
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

    def saveFirst(self, user_):
        orders = OrdersOfBTrip.objects.all()
        order_count = len(orders)
        if order_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[order_count - 1].bt_number
            cut_symb = (len(str(order_prev_num)) - 1)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись: ' + str(order_next_num_ ) + '-П '+  ' от '+ str(self.cleaned_data['bt_date'])  + '\n'  )
        log.close()
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
    'op_content',
    'op_selected']

    def saveFirst(self, user_):
        orders = OrdersOnPersonnel.objects.all().order_by('id')
        order_count = len(orders)
        if order_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[order_count - 1].op_number
            cut_symb = (len(str(order_prev_num)) - 2)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись: ' + str(order_next_num_ ) + '-ЛС '+  ' от '+ str(self.cleaned_data['op_date'])  + '\n'  )
        log.close()
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

    def saveFirst(self, user_):
        docs = OutBoundDocument.objects.all()
        docs_count = len(docs)
        if docs_count == 0:
            doc_next_num_ = 1
        else:
            doc_prev_num = docs[docs_count - 1].doc_number
            doc_next_num_ = int(doc_prev_num) + 1
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись: '+ str(self.cleaned_data['doc_type'])+ " " + str(doc_next_num_ ) +  ' от '+ str(self.cleaned_data['doc_date'])  + '\n'  )
        log.close()
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





    def saveFirst(self, user_):
        letters = LetterOfInvite.objects.all()
        letters_count = len(letters)
        if letters_count == 0:
            letter_next_num_ = 1
        else:
            letter_prev_num = letters[letters_count - 1].loi_number
            letter_next_num_ = int(letter_prev_num) + 1
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись о заявлении о приеме : ' + str(letter_next_num_) +  ' от '+ str(self.cleaned_data['loi_date']) + " принимаемый сотрудник: " + str(self.cleaned_data['loi_employee']) + '\n'  )
        log.close()
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

    def saveFirst(self, user_, year_):
        orders = LaborContract.objects.all()
        orders_count = len(orders)
        if orders_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[orders_count - 1].lc_number
            cut_symb = (len(str(order_prev_num)) - 4)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись о трудовом договоре: ' + str(order_next_num_) + " " + str(year_) +  ' от '+ str(self.cleaned_data['lc_date']) + " принимаемый сотрудник: " + str(self.cleaned_data['lc_emloyer']) + '\n'  )
        log.close()
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
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись о трудовой книжке #: ' +  str(self.cleaned_data['eh_number']) + " принимаемый сотрудник: " + str(self.cleaned_data['eh_employer']) + '\n'  )
        log.close()
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

class SickRegistry_form(forms.ModelForm):

        class Meta:
            model = SickRegistry
            fields = [
            'sr_number']

        def saveFirst(self,user_):
            registries = SickRegistry.objects.all().order_by('sr_number')
            regs_count = len(registries)
            if regs_count == 0:
                reg_next_num_ = 1
            else:
                reg_prev_num = registries[regs_count - 1].sr_number
                reg_next_num_ = int(reg_prev_num) + 1

            new_registry = SickRegistry.objects.create(
            sr_number = reg_next_num_,
            sr_res_officer = user_
            )
            return new_registry



class SickDocument_form(forms.ModelForm):
    class Meta:
        model = SickDocument

        fields = [

    'sd_number',
    'sd_emp',
    'sd_pos',
    'sd_dep',
    'sd_dur_from',
    'sd_dur_to',
    'sd_comm']




    def saveFirst(self,user_, sr_number_):
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись о больничном листе №: ' +  str(self.cleaned_data['sd_number']) + " в реестр №: "+ str(sr_number_) + '\n'  )
        log.close()
        new_doc = SickDocument.objects.create(
        sd_reg_number = sr_number_,
        sd_number = self.cleaned_data['sd_number'],
        sd_emp = self.cleaned_data['sd_emp'],
        sd_pos = self.cleaned_data['sd_pos'],
        sd_dep = self.cleaned_data['sd_dep'],
        sd_dur_from = self.cleaned_data['sd_dur_from'],
        sd_dur_to = self.cleaned_data['sd_dur_to'],
        sd_comm = self.cleaned_data['sd_comm']

        )

        return new_doc
