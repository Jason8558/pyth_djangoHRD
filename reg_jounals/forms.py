from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import *
from django.contrib.auth.forms import AuthenticationForm
import datetime as DT
from TURV.models import Employers, Department as TURVDepartment, Position as TURVPositions
from .additionals import *

def last_doc(dname):
    ld = dname.objects.latest("id")
    return ld

class LetterOfResignation_form(forms.ModelForm):
    class Meta:
        model = LetterOfResignation
        fields =['lor_date',
        
        
        'lor_dateOfRes',
       
        'lor_itemOfRes',
        'lor_additionalData']


    lor_date = forms.CharField(label="Дата подачи заявления" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату',  'type':'date'}))
    lor_dateOfRes = forms.DateField(label="Дата увольнения", required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату',  'type':'date'}))
    lor_additionalData = forms.CharField(label="Причина увольнения", required=False, widget=forms.TextInput(
        attrs={'list':'additional-metadata'}))




    def saveFirst(self, user_, bound_employer:Employers, department:TURV_departments):
        current_doc = LetterOfResignation
        letters = LetterOfResignation.objects.all()
        letters_count = len(letters)
        if letters_count == 0:
            letter_next_num_ = 1
        else:
            if self.cleaned_data['lor_date'].split("-")[0] != str(last_doc(current_doc).lor_date).split("-")[0]:
                letter_next_num_ = 1
            else:
                letter_prev_num = last_doc(current_doc).lor_number
                letter_next_num_ = int(letter_prev_num) + 1
        next_id = int(LetterOfResignation.objects.latest('id').id) + 1
        logs.objects.create(
        date = DT.datetime.now(),
        event = logs_event.objects.get(id=1),
        doc_id = next_id,
        type = 'Заявление на увольнение',
        number = str(letter_next_num_),
        doc_date = self.cleaned_data['lor_date'],
        addData = self.cleaned_data['lor_additionalData'],
        link = '/letters_of_resignation/' + str(next_id) + '/edit',
        res_officer = user_

        )

        ExistAdditionalMetadata = AdditionalMetadata.objects.filter(owner="LetterOfResignation")
       
        if not str(self.cleaned_data['lor_additionalData']).replace(" ", "") == "":
            owner = "LetterOfResignation"
            if ExistAdditionalMetadata.count() == 0:
                NewEam = AdditionalMetadata.objects.create(
                    owner = owner,
                    text = self.cleaned_data['lor_additionalData']
                )
            else: 
                for EAM in ExistAdditionalMetadata:
                    if EAM.text.replace(" ", "").lower() != str(self.cleaned_data['lor_additionalData']).replace(" ", "").lower():
                        NewEam = AdditionalMetadata.objects.create(
                            owner = owner,
                            text = self.cleaned_data['lor_additionalData']
                        )

                        NewEam.save()

        new_letter = LetterOfResignation.objects.create(
            lor_date            = self.cleaned_data['lor_date'],
            lor_number          = str(letter_next_num_),
            bound_employer      = bound_employer,
            department          = department,
            lor_employee        = None,
            lor_dateOfRes       = self.cleaned_data['lor_dateOfRes'],
            lor_additionalData  = self.cleaned_data['lor_additionalData'],
            lor_itemOfRes       = self.cleaned_data['lor_itemOfRes'],
            lor_res_officer     = user_
        )



        return new_letter

class OrdersOnOtherMatters_form(forms.ModelForm):
    class Meta:
        model = OrdersOnOtherMatters
        fields = ['oom_date',
    'oom_content']

    oom_date = forms.CharField(label="Дата приказа" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'id': 'doc_date', 'type':'date'}))
    oom_content = forms.CharField(label="Содержание", widget=forms.Textarea)

    def saveFirst(self, user_):
        current_doc = OrdersOnOtherMatters
        orders = OrdersOnOtherMatters.objects.all()
        orders_count = len(orders)
        if orders_count == 0:
            order_next_num_ = 1
        else:
            # print(str(DT.date.today().year))
            if self.cleaned_data['oom_date'].split("-")[0] != str(last_doc(current_doc).oom_date).split("-")[0]:
                order_next_num_ = 1
            else:
                order_prev_num = last_doc(current_doc).oom_number
                cut_symb = (len(str(order_prev_num)) - 2)
                order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        next_id = int(OrdersOnOtherMatters.objects.latest('id').id) + 1
        logs.objects.create(
        date = DT.datetime.now(),
        event = logs_event.objects.get(id=1),
        doc_id = next_id,
        type = 'Приказ по другим вопросам',
        number = str(order_next_num_) + "К",
        doc_date = self.cleaned_data['oom_date'],
        addData = '',
        link = '/orders_on_others/' + str(next_id) + '/edit',
        res_officer = user_

        )

        new_order = OrdersOnOtherMatters.objects.create(
            oom_number = str(order_next_num_) + "-К",
            oom_date = self.cleaned_data['oom_date'],
            oom_content = self.cleaned_data['oom_content'],
            oom_res_officer = user_
        )

        return new_order

# старые приказы на отпуск
class OrdersOnVacation_form(forms.ModelForm):
    class Meta:
        model = OrdersOnVacation
        fields = ['oov_date',
    'oov_empList']

    oov_date = forms.CharField(label="Дата приказа" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'id': '', 'type':'date'}))

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
#############################################

class OrdersOfBTrip_form(forms.ModelForm):
    class Meta:
        model = OrdersOfBTrip
        fields = [
    'bt_date',
    'bt_emloyer',
    'bt_place',
    'bt_dep',
    'bt_dur_from',
    'bt_dur_to'
    ]

    bt_date = forms.CharField(label="Дата приказа" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))
    bt_dur_from = forms.CharField(label="Дата начала командировки" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))

    bt_dur_to = forms.CharField(label="Дата завершения командировки" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))

    def saveFirst(self, user_, employer_id:int, department_id:int):
        current_doc = OrdersOfBTrip
        orders = OrdersOfBTrip.objects.all()
        order_count = len(orders)
        if order_count == 0:
            order_next_num_ = 1
        else:
            if self.cleaned_data['bt_date'].split("-")[0] != str(last_doc(current_doc).bt_date).split("-")[0]:
                order_next_num_ = 1
            else:
                order_prev_num = orders[order_count - 1].bt_number
                cut_symb = (len(str(order_prev_num)) - 1)
                order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        next_id = int(OrdersOfBTrip.objects.latest('id').id) + 1
        
        # Запись в лог
        logs.objects.create(
            date        = DT.datetime.now(),
            event       = logs_event.objects.get(id=1),
            doc_id      = next_id,
            type        = 'Приказ на командировку',
            number      = str(order_next_num_) + "П",
            doc_date    = self.cleaned_data['bt_date'],
            addData     = '',
            link        = '/orders_of_BTrip/' + str(next_id) + '/upd',
            res_officer = user_
        )

       

        new_order = OrdersOfBTrip.objects.create(
            bound_employer  = get_employer_from_db(employer_id),
            department      = get_department_from_db(department_id),
            bt_date         = self.cleaned_data['bt_date'],
            bt_number       = str(order_next_num_) + "П",
            bt_place        = self.cleaned_data['bt_place'],
            bt_dur_from     = self.cleaned_data['bt_dur_from'],
            bt_dur_to       = self.cleaned_data['bt_dur_to'],
            bt_res_officer  = user_
        )

        return new_order

class OrdersOnPersonnel_form(forms.ModelForm):
    class Meta:
        model = OrdersOnPersonnel
        fields = [
    'grounds_for_resignation',
    'bound_employer',
    'op_date',
    'op_dateOfInv',
    'op_dateOfRes',
    'op_typeOfWork',
    'op_probation',
    'op_type',
    'op_dep',
    'op_emloyer',
    'op_content',
    'op_lastcheck',
    'op_selected']

    # employers = Employers.objects.none()
    
    op_date = forms.CharField(label="Дата приказа" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату',  'type':'date'}))
    op_emloyer = forms.CharField(label='ФИО сотрудника (полностью!)*', required=False, widget=forms.TextInput(
    attrs={'onchange':'sfio()', 'required':False}
    ))
    op_dateOfInv = forms.CharField(label="Дата приема на работу" , required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату',  'type':'date', 'value':'01.01.0002'}))

    op_dateOfRes = forms.CharField(label="Дата увольнения" , required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату',  'type':'date', 'value':'01.01.0002'}))

    op_moveFrom = forms.CharField(label="Перевод с" , required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату',  'type':'date'}))

    op_moveTo = forms.CharField(label="по" , required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату',  'type':'date'}))
    
    # bound_employer = forms.ChoiceField(widget=forms.Select(attrs={'id':'order-of-personell-bound-employer-field'}))
    

    

    def saveFirst(self, user_, bound_employer_id:int, department_id:int):
        if bound_employer_id:
            bound_employer = Employers.objects.get(id=bound_employer_id)
        else:
            bound_employer = None
        
        current_doc     = last_doc(OrdersOnPersonnel)
        orders          = OrdersOnPersonnel.objects.all().order_by('id')
        order_count     = len(orders)
        
        if order_count == 0:
            order_next_num_ = 1
        else:
            if self.cleaned_data['op_date'].split("-")[0] != str(current_doc.op_date).split("-")[0]:
                order_next_num_ = 1
            else:
                order_prev_num = orders[order_count - 1].op_number
                cut_symb = (len(str(order_prev_num)) - 2)
                order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        next_id = int(OrdersOnPersonnel.objects.latest('id').id) + 1
        
        logs.objects.create(
        date        = DT.datetime.now(),
        event       = logs_event.objects.get(id=1),
        doc_id      = next_id,
        type        = 'Приказ по личному составу',
        number      = str(order_next_num_) + 'ЛС',
        doc_date    = self.cleaned_data['op_date'],
        addData     = '',
        link        = '/orders_on_personnel/' + str(next_id) + '/upd',
        res_officer = user_
        )

        if self.cleaned_data['op_dateOfInv'] == "":
            dateofInv = '0001-01-01'
        else:
            dateofInv = self.cleaned_data['op_dateOfInv']

        if self.cleaned_data['op_dateOfRes'] == "":
            dateofRes = '0001-01-01'
        else:
            dateofRes = self.cleaned_data['op_dateOfRes']

        if self.cleaned_data['op_moveFrom'] == "":
            moveFrom = '0001-01-01'
        else:
            moveFrom = self.cleaned_data['op_moveFrom']

        if self.cleaned_data['op_moveTo'] == "":
            moveTo = '0001-01-01'
        else:
            moveTo = self.cleaned_data['op_moveTo']

        if department_id:
            department = TURVDepartment.objects.get(id=department_id)
        else:
            department = None
        
        

        new_order = OrdersOnPersonnel.objects.create(
            
            department                  = department,
            bound_employer              = bound_employer,
            grounds_for_resignation     = self.cleaned_data['grounds_for_resignation'],
            op_date                     = self.cleaned_data['op_date'],
            op_type                     = self.cleaned_data['op_type'],
            op_dateOfInv                = dateofInv,
            op_dateOfRes                = dateofRes,
            op_typeOfWork               = self.cleaned_data['op_typeOfWork'],
            op_probation                = self.cleaned_data['op_probation'],
            op_moveFrom                 = moveFrom,
            op_moveTo                   = moveTo,
            op_number                   = str(order_next_num_)+"ЛС",
            # op_dep                      = self.cleaned_data['op_dep'],
            op_content                  = self.cleaned_data['op_content'],
            op_emloyer                  = self.cleaned_data['op_emloyer'],
            op_res_officer              = user_
        )

        return new_order
    
  

        

class OutBoundDocument_form(forms.ModelForm):
    class Meta:
        model = OutBoundDocument
        fields = ['doc_type',
    'doc_date',
    'doc_dest',
    'doc_additionalData']

    doc_date = forms.CharField(label="Дата документа" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))

    def saveFirst(self, user_):
        current_doc = last_doc(OutBoundDocument)
        docs = OutBoundDocument.objects.all()
        docs_count = len(docs)
        if docs_count == 0:
            doc_next_num_ = 1
        else:
            if self.cleaned_data['doc_date'].split("-")[0] != str(current_doc.doc_date).split("-")[0]:
                doc_next_num_ = 1
            else:
                doc_prev_num = docs[docs_count - 1].doc_number
                doc_next_num_ = int(doc_prev_num) + 1

        next_id = int(OutBoundDocument.objects.latest('id').id) + 1
        logs.objects.create(
        date = DT.datetime.now(),
        event = logs_event.objects.get(id=1),
        doc_id = next_id,
        type = 'Исходящий документ',
        number = str(doc_next_num_),
        doc_date = self.cleaned_data['doc_date'],
        addData = self.cleaned_data['doc_type'],
        link = '/outbound_docs/' + str(next_id) + '/edit',
        res_officer = user_
        )

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
        attrs={'class': 'lform-input loginField', 'placeholder': '(как в почте, только без @pkvoda.ru)', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'lform-input pwdField',
            'placeholder': '(как на компьютере)',
            'id': 'hi',
        }
))

class LetterOfInvite_form(forms.ModelForm):
    class Meta:
        model = LetterOfInvite
        fields = [ 
                'loi_date',
                'loi_employee',
                'loi_position',
                'loi_department',
                'loi_dateOfInv',
                'loi_additionalData',
                'reason'
                ]

    loi_date = forms.CharField(label="Дата документа" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату',  'type':'date'}))
    loi_dateOfInv = forms.DateField(label="Дата приема" , required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату',  'type':'date'}))
    reason = forms.CharField(label="Причина", required=False, widget=forms.TextInput(
        attrs={'list':'additional-metadata'}))

    def saveFirst(self, user_, department:TURVDepartment, position:TURVPositions):
        current_doc = last_doc(LetterOfInvite)
        letters = LetterOfInvite.objects.all()
        letters_count = len(letters)
        if letters_count == 0:
            letter_next_num_ = 1
        else:
            if self.cleaned_data['loi_date'].split("-")[0] != str(current_doc.loi_date).split("-")[0]:
                letter_next_num_ = 1
            else:
                letter_prev_num = letters[letters_count - 1].loi_number
                letter_next_num_ = int(letter_prev_num) + 1


        next_id = int(LetterOfInvite.objects.latest('id').id) + 1
        logs.objects.create(
        date = DT.datetime.now(),
        event = logs_event.objects.get(id=1),
        doc_id = next_id,
        type = 'Заявление на прием',
        number = str(letter_next_num_),
        doc_date = self.cleaned_data['loi_date'],
        addData = '',
        link = '/letters_of_invite/' + str(next_id) + '/edit',
        res_officer = user_
        )

        ExistAdditionalMetadata = AdditionalMetadata.objects.filter(owner="LetterOfInvite")
       
        if not str(self.cleaned_data['reason']).replace(" ", "") == "":
            owner = "LetterOfInvite"
            if ExistAdditionalMetadata.count() == 0:
                NewEam = AdditionalMetadata.objects.create(
                    owner = owner,
                    text = self.cleaned_data['reason']
                )
            else: 
                for EAM in ExistAdditionalMetadata:
                    if EAM.text.replace(" ", "").lower() != str(self.cleaned_data['reason']).replace(" ", "").lower():
                        NewEam = AdditionalMetadata.objects.create(
                            owner = owner,
                            text = self.cleaned_data['reason']
                        )

                        NewEam.save()

        new_letter = LetterOfInvite.objects.create(
            loi_date            = self.cleaned_data['loi_date'],
            loi_number          = str(letter_next_num_),
            loi_employee        = self.cleaned_data['loi_employee'],
            position            = position,
            department          = department,
            loi_dateOfInv       = self.cleaned_data['loi_dateOfInv'],
            loi_additionalData  = self.cleaned_data['loi_additionalData'],
            reason              = self.cleaned_data['reason'],
            loi_res_officer     = user_
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

    lc_date = forms.CharField(label="Дата договора" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))
    lc_dateOfInv = forms.CharField(label="Дата приема на работу" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))

    def saveFirst(self, user_, year_, bound_employer:Employers, department:TURVDepartment, position:TURVPositions):
        current_doc = last_doc(LaborContract)
        orders = LaborContract.objects.all()
        orders_count = len(orders)
        if orders_count == 0:
            order_next_num_ = 1
        else:
            if self.cleaned_data['lc_date'].split("-")[0] != str(current_doc.lc_date).split("-")[0]:
                order_next_num_ = 1
            else:
                order_prev_num = orders[orders_count - 1].lc_number
                cut_symb = (len(str(order_prev_num)) - 4)
                order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        next_id = int(LaborContract.objects.latest('id').id) + 1
        
        logs.objects.create(
            
            date        = DT.datetime.now(),
            event       = logs_event.objects.get(id=1),
            doc_id      = next_id,
            type        = 'Трудовой договор',
            number      = str(order_next_num_)+"("+str(year_)+")",
            doc_date    = self.cleaned_data['lc_date'],
            addData     = '',
            link        = '/laborContracts/' + str(next_id) + '/upd',
            res_officer = user_
        )


        new_contract = LaborContract.objects.create(
            lc_date             = self.cleaned_data['lc_date'],
            lc_number           = str(order_next_num_)+"("+str(year_)+")",
            position            = position,
            department          = department,
            lc_dateOfInv        = self.cleaned_data['lc_dateOfInv'],
            lc_workCond         = self.cleaned_data['lc_workCond'],
            bound_employer      = bound_employer,
            lc_res_officer      = user_
        )

        return new_contract

class EmploymentHistory_form(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = [
            'eh_isdigital',
            'eh_number',
            'eh_dateOfInv',
            'eh_OrderInv',
            'eh_employer',
            'eh_pos',
            'eh_dep',
            'eh_dateOfResign',
            'eh_OrderResign']

    eh_isdigital = forms.BooleanField(label="Электронная",required=False, widget=forms.CheckboxInput(attrs={'onclick':'digital_histories()'}))
    eh_dateOfInv = forms.CharField(label="Дата приема на работу" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))
    eh_dateOfResign = forms.DateField(label="Дата увольнения" , required=False,  widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))


    def saveFirst(self, user_, department:TURVDepartment):
        next_id = int(EmploymentHistory.objects.latest('id').id) + 1
        logs.objects.create(
        date = DT.datetime.now(),
        event = logs_event.objects.get(id=1),
        doc_id = next_id,
        type = 'Трудовая книжка',
        number = self.cleaned_data['eh_number'],
        doc_date = DT.datetime.now(),
        addData = '',
        link = '/employment_history/' + str(next_id) + '/upd',
        res_officer = user_
        )



        new_empHistory = EmploymentHistory.objects.create(
            eh_isdigital = self.cleaned_data['eh_isdigital'],
            eh_number = self.cleaned_data['eh_number'],
            eh_dateOfInv = self.cleaned_data['eh_dateOfInv'],
            eh_employer = self.cleaned_data['eh_employer'],
            eh_pos = self.cleaned_data['eh_pos'],
            department = department,
            eh_OrderInv = self.cleaned_data['eh_OrderInv'],
            eh_OrderResign = self.cleaned_data['eh_OrderResign'],
            eh_dateOfResign = self.cleaned_data['eh_dateOfResign'],
            eh_res_officer = user_ 
        )

        return new_empHistory

class SickRegistry_form(forms.ModelForm):

        class Meta:
            model = SickRegistry
            fields = [
            'sr_number']

        def saveFirst(self,user_,year_):
            current_doc = last_doc(SickRegistry)
            registries = SickRegistry.objects.all().order_by('sr_number')
            regs_count = len(registries)
            if regs_count == 0:
                reg_next_num_ = 1
            else:

                if str(year_) != str(current_doc.sr_year):
                    reg_next_num_ = 1
                else:
                    reg_prev_num = current_doc.sr_number
                    reg_next_num_ = int(reg_prev_num) + 1
            #
            # next_id = int(LetterOfInvite.objects.latest('id').id) + 1
            # logs.objects.create(
            # date = DT.datetime.now(),
            # event = logs_event.objects.get(id=1),
            # doc_id = next_id,
            # type = 'Реестр б\л',
            # number = self.cleaned_data['eh_number'],,
            # doc_date = '',
            # addData = '',
            # link = '/employment_history/' + str(next_id) + '/upd',
            # res_officer = user_
            # )

            new_registry = SickRegistry.objects.create(
            sr_number = reg_next_num_,
            sr_res_officer = user_,
            sr_year = int(DT.datetime.today().year)
            )
            return new_registry

class SickDocument_form(forms.ModelForm):

    class Meta:


        model = SickDocument
        error_messages = {
            NON_FIELD_ERRORS: {
            'unique_together': "Больничный лист с таким номером существует!",
            }
                }
        fields = [

    'sd_number',
    'sd_emp',
    'sd_pos',
    'sd_dep',
    'sd_dur_from',
    'sd_dur_to',
    'sd_comm']

    sd_dur_from = forms.DateField(label="Дата начала болезни" ,  widget=forms.TextInput(
        attrs={'type':'date'}))
    sd_dur_to = forms.DateField(label="Дата окончания болезни" ,  widget=forms.TextInput(
        attrs={'type':'date'}))




    def saveFirst(self,user_, id):
        sr_number_ = SickRegistry.objects.get(id=id).sr_number
        print(sr_number_)
        log = open('log.txt', 'a')
        log.write(str(DT.date.today()) + " пользователь " +str(user_) + ' внес запись о больничном листе №: ' +  str(self.cleaned_data['sd_number']) + " в реестр №: "+ str(sr_number_) + '\n'  )
        log.close()
        new_doc = SickDocument.objects.create(

        sd_number = self.cleaned_data['sd_number'],
        sd_emp = self.cleaned_data['sd_emp'],
        sd_pos = self.cleaned_data['sd_pos'],
        sd_dep = self.cleaned_data['sd_dep'],
        sd_dur_from = self.cleaned_data['sd_dur_from'],
        sd_dur_to = self.cleaned_data['sd_dur_to'],
        sd_comm = self.cleaned_data['sd_comm'],
        sd_bound_reg_id = id

        )

        return new_doc

class NewOrdersOnVacation_form(forms.ModelForm):
    class Meta:
        model = NewOrdersOnVacation
        fields = ['order_date']

    order_date = forms.DateField(label="Дата приказа" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))

    def saveFirst(self, user_):
        current_doc = last_doc(NewOrdersOnVacation)
        orders = NewOrdersOnVacation.objects.all().order_by('id')
        orders_count = len(orders)

        if orders_count == 0:
            order_next_num_ = 1
        else:
            if str(self.cleaned_data['order_date']).split("-")[0] != str(current_doc.order_date).split("-")[0]:
                order_next_num_ = 1
            else:
                order_prev_num = current_doc.order_number
                cut_symb = (len(str(order_prev_num)) - 6)
                order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        new_order = NewOrdersOnVacation.objects.create(
            order_date = self.cleaned_data['order_date'],
            order_number = str(order_next_num_) + '-К-ОТП' ,
            res_officer = user_
        )

        return new_order

class NewOrdersOnVacationItem_form(forms.ModelForm):
    class Meta:
        model = NewOrdersOnVacation_item
        fields = ['fio', 'dep', 'dur_from', 'days_count', 'dur_to',  'vac_type', 'comm']

    dur_from = forms.DateField(label="Дата начала отпуска" , required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))

    days_count = forms.CharField(label="Количество дней отпуска" ,required=False, widget=forms.TextInput(
    attrs={'onchange':'duration()', 'type':'text'}))

    dur_to = forms.DateField(label="Дата окончания отпуска" , required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date', 'onchange':'vac_calc()'}))


    def saveFirst(self, order_id, user_, bound_employer:Employers, department:TURVDepartment):
        order = NewOrdersOnVacation.objects.get(id=order_id)
        next_id = int(NewOrdersOnVacation_item.objects.latest('id').id) + 1

        logs.objects.create(
            date        = DT.datetime.now(),
            event       = logs_event.objects.get(id=1),
            doc_id      = next_id,
            type        = 'Запись в приказе на отпуск',
            number      = order.order_number,
            doc_date    = order.order_date,
            addData     = 'Приказ: ' + order.order_number + ' ' + str(order.order_date),
            link        = '/orders_on_vacation_new/upditem' + str(next_id),
            res_officer = user_
                )
        
        new_item = NewOrdersOnVacation_item.objects.create(
            bound_order_id  = order_id,
            bound_employer  = bound_employer,
            department_new      = department,
            dur_from        = self.cleaned_data['dur_from'],
            dur_to          = self.cleaned_data['dur_to'],
            days_count      = self.cleaned_data['days_count'],
            vac_type        = self.cleaned_data['vac_type'],
            comm            = self.cleaned_data['comm']

        )

        return new_item

class Identity_form(forms.ModelForm):
    class Meta:
        model = Identity
        fields = [
        # 'number',
    'date_giving',
    'employer']

    number = forms.CharField(label="" ,required=False, widget=forms.TextInput(
        attrs={'type':'text', 'style':'display:none'}))

    date_giving = forms.DateField(label="Дата выдачи" , widget=forms.TextInput(
        attrs={'placeholder': 'Введите дату', 'type':'date'}))

    def saveFirst(self, user_, bound_employer:Employers, department:TURVDepartment):
        ind = Identity.objects.all().order_by("id")
        ind_count = len(ind)

        if ind_count == 0:
            ind_next_num_ = 1
        else:
            ind_prev_num = ind[ind_count - 1].number
            ind_next_num_ = int(ind_prev_num) + 1

        next_id = int(Identity.objects.latest('id').id) + 1

        logs.objects.create(
        date = DT.datetime.now(),
        event = logs_event.objects.get(id=1),
        doc_id = next_id,
        type = 'Удостоверение',
        number = next_id,
        doc_date = self.cleaned_data['date_giving'],
        addData = '',
        link = '/identity/upd' + str(next_id),
        res_officer = user_
                )

        new_identity = Identity.objects.create(
            number          = ind_next_num_,
            date_giving     = self.cleaned_data['date_giving'],
            bound_employer  = bound_employer,
            department_new      = department,
            res_officer     = user_
        )

        return new_identity
