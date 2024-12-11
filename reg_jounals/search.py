from .models import NewOrdersOnVacation_item as Vacations
from .models import OrdersOfBTrip as BuisnessTrip
from .models import LetterOfInvite as LettersOfInvite
from .models import EmploymentHistory
from .models import OrdersOnOtherMatters as OrdersOfOthers
from .models import OutBoundDocument as OutboundDocuments
from .models import OrdersOnPersonnel
from .models import LaborContract as LaborContracts
from .models import LetterOfResignation as LettersOfResiganton
from .models import Identity as Identitys


def search(fields):

    # Параметры поиска

    # Тип документа
    document_type = fields['document_type']

    # Общие
    name = fields['name']
    department      = fields['department']
    period_from     = fields['period_from']
    period_to       = fields['period_to']
    reason          = fields['reason']

    # если приходят пустые даты
    if period_from == '':
        period_from = '0001-01-01'

    if period_to == '':
        period_to = '3999-12-31'
    # ------------------------------

    if int(document_type) == 1:
        # Отпуск
        vacation_type = fields['vacation_type']

        search_result = Vacations.objects.filter(bound_employer__fullname__icontains=name).filter(vac_type__icontains=vacation_type).filter(
            bound_order__order_date__gte=period_from, bound_order__order_date__lte=period_to).order_by('-bound_order__order_date')

        if department:
           search_result = search_result.filter(department_new=department)

    if int(document_type) == 2:
         # Командировки
        destination = fields['destination']

        search_result = BuisnessTrip.objects.filter(bound_employer__fullname__icontains=name).filter(
            bt_date__gte=period_from, bt_date__lte=period_to).filter(bt_place__icontains=destination).order_by('-bt_date')
        
        # search_result_2 = BuisnessTrip.objects.filter(bt_emloyer__icontains=name).filter(
        #     bt_date__gte=period_from, bt_date__lte=period_to).filter(bt_place__icontains=destination).order_by('-bt_date')

        # search_result = search_result_1.union(search_result_2).order_by('-bt_date')

        if department:
            search_result = search_result.filter(department_id=department)

    if int(document_type) == 3:
        # Заявления на прием

        search_result = LettersOfInvite.objects.filter(loi_employee__icontains=name).filter(
            loi_date__gte=period_from, loi_date__lte=period_to).order_by('-loi_date')

        if department:
            search_result = search_result.filter(department=department)
        
        if reason:
            search_result = search_result.filter(reason__iexact=reason)

    if int(document_type) == 4:
        # Трудовые книжки
        employment_history_type = fields['employment_history_type']

        search_result = EmploymentHistory.objects.filter(eh_employer__icontains=name).filter(
            eh_dateOfInv__gte=period_from, eh_dateOfInv__lte=period_to).order_by('-eh_dateOfInv')
        
        if department:
            search_result = search_result.filter(department=department)

        if employment_history_type:
            search_result = search_result.filter(eh_isdigital=employment_history_type)

    if int(document_type) == 5:
        # Приказы по другим вопросам
        content                         = fields['content']
        orders_of_others_res_officier   = fields['orders_of_others_res_officier']

        search_result = OrdersOfOthers.objects.filter(oom_number__icontains=name).filter(oom_content__icontains=content).filter(
        oom_date__gte=period_from, oom_date__lte=period_to).order_by('-oom_date')

        if orders_of_others_res_officier:
            search_result = search_result.filter(oom_res_officer=orders_of_others_res_officier)
    
    if int(document_type) == 6:
        # Исходящие документы
        
        destination                     = fields['destination']
        outbound_document_type          = fields['outbound_document_type']

        search_result = OutboundDocuments.objects.filter(doc_dest__icontains=destination).filter(doc_type__icontains=outbound_document_type).filter(
        doc_date__gte=period_from, doc_date__lte=period_to).order_by('-doc_date')

    if int(document_type) == 7:
        # Приказы по личному составу
        orders_of_personnel_event       = fields['orders_on_personnel_event']
        content                         = fields['content']
        orders_on_personnel_number      = fields['orders_on_personnel_number']



        search_result = OrdersOnPersonnel.objects.filter(op_emloyer__icontains=name).filter(op_number__icontains=orders_on_personnel_number).filter(
        op_date__gte=period_from, op_date__lte=period_to).filter(op_content__icontains=content).order_by('-op_date')

        if orders_of_personnel_event:
            search_result = search_result.filter(op_type = orders_of_personnel_event)
        
        if department:
            search_result = search_result.filter(department=department)

        search_result_2 = OrdersOnPersonnel.objects.filter(bound_employer__fullname__icontains=name).filter(op_number__icontains=orders_on_personnel_number).filter(
        op_date__gte=period_from, op_date__lte=period_to).filter(op_content__icontains=content).order_by('-op_date')

        if orders_of_personnel_event:
            search_result_2 = search_result.filter(op_type = orders_of_personnel_event)
        
        if department:
            search_result_2 = search_result.filter(department=department)
        
        search_result = search_result.union(search_result_2).order_by('-op_date')

    if int(document_type) == 8:
        # Трудовые договоры
        search_result = LaborContracts.objects.filter(bound_employer__fullname__icontains=name).filter(
            lc_date__gte=period_from, lc_date__lte=period_to).order_by('-lc_date')

        if department:
            search_result = search_result.filter(department = department)

    if int(document_type) == 9:
        # Заявления на увольнения
        resignation_from    = fields['resignation_from']
        resignation_to      = fields['resignation_to']
        

        if resignation_from == '':
            resignation_from = '0001-01-01'

        if resignation_to == '':
            resignation_to = '3999-12-31'

        search_result = LettersOfResiganton.objects.filter(
            bound_employer__fullname__icontains=name).filter(
            lor_date__gte=period_from, lor_date__lte=period_to).filter(
            lor_dateOfRes__gte=resignation_from, lor_dateOfRes__lte=resignation_to).order_by('-lor_date')

        if department:
            search_result = search_result.filter(department = department)
        
        if reason:
            search_result = search_result.filter(lor_additionalData__iexact=reason)

    if int(document_type) == 10:
        # Удостоверения
        search_result = Identitys.objects.filter(
            bound_employer__fullname__icontains=name).filter(
            date_giving__gte=period_from, date_giving__lte=period_to).order_by('-date_giving')

        if department:
            search_result = search_result.filter(department_new = department)            

    return (search_result)

