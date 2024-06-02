from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
import datetime as DT
from itertools import groupby
from django.contrib.auth.models import *
from .forms import last_doc
from TURV.models import Department as TDep
from TURV.models import Position as TPos
from TURV.models import Employers as TEmps
from TURV.models import Overtime as TOt
from .search import *
from django.contrib.auth.decorators import login_required
import json
from .additionals import create_or_update_employer

def get_user_name(request):
    username = request.user.first_name
    return JsonResponse(username, safe=False)

def index(request):

    if request.user.is_authenticated:
        ref_edit_role = False
        user_ = request.user
        u_group = user_.groups.all()
        for group in u_group:
            if (group.name == 'Табельщик') or (group.name == 'Сотрудник РО') :
                return redirect('/turv/')
            if group.name == 'Редактирование справочников':
                ref_edit_role = True
       
       
        user_io = request.user.first_name.split(' ')
        if len(user_io) < 3:
            user_io = str(user_io[0])
        else:
            user_io = str(user_io[1]) + " " +str(user_io[2])
        return render(request, 'reg_jounals/index.html', context={'user_io':user_io, 'ref_edit_role':ref_edit_role})
    else:
        return redirect('/accounts/login/')

def logfile(request):
    if request.user.is_authenticated:
        logfile = open('log.txt')
        log = []
        for line in logfile:
            log.append(line)
    return render(request, 'reg_jounals/log.html', context={'log':log})

# Исходящие документы -----------------------
def outbound_docs(request):
    if request.user.is_authenticated:
        auth = request.user.is_authenticated
        date_from = request.GET.get('doc_search_from','')
        date_to = request.GET.get('doc_search_to', '')
        
        search_query = {
            'document_type':            6,
            'outbound_document_type':   request.GET.get('outbound-documents-search-type',''),
            'name':                    '',
            'destination':              request.GET.get('outbound-documents-search-destination', ''),
            'period_from':              request.GET.get('orders-of-buisness-trip-search-from',''),
            'period_to':                request.GET.get('orders-of-buisness-trip-search-to',''),
            'department':               ''
        }
       
        if int(request.GET.get('search-sign', '0')) == 1:
            documents = search(search_query)
            p_documents = Paginator(documents, 1000)
            page_number = request.GET.get('page', 1)

        else:
            documents = OutBoundDocument.objects.all().order_by('-id')
            p_documents = Paginator(documents, 20)
            page_number = request.GET.get('page', 1)
        
        page = p_documents.get_page(page_number)
        i = 0

        return render(request, 'reg_jounals/outbound_docs.html', context={'documents':page,'auth':auth, 'i':i})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OutBoundDocument(request):
    if request.user.is_authenticated:
        documents = OutBoundDocument.objects.all()
        docs_count = len(documents)
        if docs_count == 0:
            doc_next_num_ = 1
        else:
            doc_prev_num = documents[docs_count - 1].doc_number
            doc_next_num_ = int(doc_prev_num) + 1
        if request.method == "POST":
            doc_form = OutBoundDocument_form(request.POST)
            if doc_form.is_valid():
                user_ = request.user.first_name

                doc_form.saveFirst(user_)
                return redirect('../outbound_docs/')
        else:
            doc_form = OutBoundDocument_form()
        return render(request, 'reg_jounals/outboundDocs_add.html', {'form':doc_form, 'next_num':doc_next_num_})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def upd_OutBoundDocument(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            document = OutBoundDocument.objects.get(id__iexact=id)
            bound_form = OutBoundDocument_form(instance=document)
            return render(request, 'reg_jounals/outboundDocs_upd.html', context={'form':bound_form, 'document':document})
        else:
            document = OutBoundDocument.objects.get(id__iexact=id)
            bound_form =OutBoundDocument_form(request.POST, instance=document)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/outbound_docs/')

def del_OutBoundDocument(request, id):
    if request.user.is_authenticated:
        document = OutBoundDocument.objects.get(id__iexact=id)
        document.delete()
        return redirect('/outbound_docs/')

# Заявления на увольнения -----------------------
def letter_of_resignation(request):
    if request.user.is_authenticated:
        
        deps = TDep.objects.filter(notused=0).filter(is_aup=0).order_by('name')

        if int(request.GET.get('search-sign', '0')) == 1:
            search_query = {
                'document_type':    9,
                'name':             request.GET.get('lor_search', ''),
                'period_from':      request.GET.get('letters-of-resignation-search-from',''),
                'period_to':        request.GET.get('letters-of-resignation-search-to',''),
                'resignation_from': request.GET.get('letters-of-resignation-search-date-of-resigantion-from',''),
                'resignation_to':   request.GET.get('letters-of-resignation-search-date-of-resigantion-to',''),
                'department':       request.GET.get('letters-of-resignation-search-department','')
            }
            
            letters = search(search_query)
            p_letters = Paginator(letters, 1000)
            page_number = request.GET.get('page', 1)

        else:
            letters = LetterOfResignation.objects.all().order_by('-id')
            p_letters = Paginator(letters, 20)
            page_number = request.GET.get('page', 1)
       
        page = p_letters.get_page(page_number)
        count = len(letters)

        return render(request, 'reg_jounals/letters_of_resignation.html', context={'letters':page, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_LetterOfResignation(request):
    if request.user.is_authenticated:
        # pos = TPos.objects.all()
        letter_form = LetterOfResignation_form()
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        letters = LetterOfResignation.objects.all()
        letters_count = len(letters)
        if letters_count == 0:
            letter_next_num_ = 1
        else:
            letter_prev_num = letters[letters_count - 1].lor_number
            letter_next_num_ = int(letter_prev_num) + 1
        
        if request.method == "POST":
            # получаем нестандартные реквизиты
            bound_employer  = get_employer_from_db(request.POST.get('resignation-employer-field', ''))
            department      = get_department_from_db(request.POST.get('resignation-department-field', ''))
            # position        = get_position_from_db(request.POST.get('resignation-position-field', ''))

            letter_form = LetterOfResignation_form(request.POST)
            if letter_form.is_valid():
                user_ = request.user.first_name
                letter_form.saveFirst(user_,bound_employer, department)
                return redirect('../letters_of_resignation/')
        else:

            return render(request, 'reg_jounals/LetterOfResignation_add.html', context={'form':letter_form, 'next_num':letter_next_num_, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def upd_LetterOfResignation(request, id):
    if request.user.is_authenticated:
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        letter = LetterOfResignation.objects.get(id__iexact=id)
       
        if request.method == "GET":
            
            bound_form = LetterOfResignation_form(instance=letter)
            return render(request, 'reg_jounals/LetterOfResignation_upd.html', context={'form':bound_form, 'letter':letter, 'deps':deps})
        else:
            updated_bound_employer  = get_employer_from_db(request.POST.get('resignation-employer-field', ''))
            updated_department      = get_department_from_db(request.POST.get('resignation-department-field', ''))
            
            bound_form = LetterOfResignation_form(request.POST, instance=letter)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()

                if updated_bound_employer != new_obj.bound_employer:
                    new_obj.bound_employer = updated_bound_employer
                    new_obj.save()
                
                if updated_department != new_obj.department:
                    new_obj.department = updated_department
                    new_obj.save()

                return redirect('/letters_of_resignation')

def del_LetterOfResignation(request, id):
    if request.user.is_authenticated:
        letter = LetterOfResignation.objects.get(id__iexact=id)
        letter.delete()
        return redirect('/letters_of_resignation')

# Заявления на прием ------------------------------
def letter_of_invite(request):
        if request.user.is_authenticated:
            
            deps = TDep.objects.filter(notused=0).filter(is_aup=0)

            if int(request.GET.get('search-sign', '0')) == 1:
                search_query = {
                    'document_type':    3,
                    'name':             request.GET.get('loi_search', ''),
                    'period_from':      request.GET.get('letters-of-invite-search-from',''),
                    'period_to':        request.GET.get('letters-of-invite-search-to',''),
                    'department':       request.GET.get('letters-of-invite-search-department','')
                }

                letters = search(search_query)
                p_letters = Paginator(letters, 10000)
                page_number = request.GET.get('page', 1)
                page = p_letters.get_page(page_number)
            else:
                letters = LetterOfInvite.objects.all().order_by('-id')
                p_letters = Paginator(letters, 20)
                page_number = request.GET.get('page', 1)
                page = p_letters.get_page(page_number)
                count = len(letters)


            return render(request, 'reg_jounals/letters_of_invite.html', context={'letters':page, 'deps':deps})
        else:
            return render(request, 'reg_jounals/no_auth.html')

def upd_LetterOfInvite(request, id):
    if request.user.is_authenticated:
        pos     = TPos.objects.all()
        deps    = TDep.objects.filter(notused=0).filter(is_aup=0)
        letter  = LetterOfInvite.objects.get(id__iexact=id)
        
        if request.method == "GET":
            
            bound_form = LetterOfInvite_form(instance=letter)
            return render(request, 'reg_jounals/LetterOfInvite_upd.html', context={'form':bound_form, 'letter':letter, 'pos':pos, 'deps':deps})
        else:
            
            bound_form = LetterOfInvite_form(request.POST, instance=letter)

            updated_department  = get_department_from_db(request.POST.get('invite-department-field', ''))
            updated_position    = get_position_from_db(request.POST.get('sel_pos',''))

            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()

                if updated_department != new_obj.department:
                    new_obj.department = updated_department
                    new_obj.save()
                
                if updated_position != new_obj.position:
                    new_obj.position = updated_position
                    new_obj.save()               


                return redirect('/letters_of_invite')

def nr_LetterOfInvite(request):
    if request.user.is_authenticated:
        pos = TPos.objects.all()
        letter_form = LetterOfInvite_form()
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        letters = LetterOfInvite.objects.all()
        letters_count = len(letters)
        if letters_count == 0:
            letter_next_num_ = 1
        else:
            letter_prev_num = letters[letters_count - 1].loi_number
            letter_next_num_ = int(letter_prev_num) + 1
        if request.method == 'POST':
            letter_form = LetterOfInvite_form(request.POST)
            
            department  = get_department_from_db(request.POST.get('invite-department-field',''))
            position    = get_position_from_db(request.POST.get('sel_pos', ''))

            if letter_form.is_valid():
                user_ = request.user.first_name
                letter_form.saveFirst(user_, department, position)
                return redirect('../letters_of_invite/')
        return render(request, 'reg_jounals/LetterOfInvite_add.html', context={'form':letter_form, 'next_num':letter_next_num_, 'pos':pos, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def del_LetterOfInvite(request, id):
    if request.user.is_authenticated:
        letter = LetterOfInvite.objects.get(id__iexact=id)
        letter.delete()
        return redirect('/letters_of_invite')

# Приказы по другим вопросам -----------------------
def order_other_matters(request):
    if request.user.is_authenticated:
        group = Group.objects.get(name__icontains='Сотрудник СУП')
        users = group.user_set.all()

        res_users = User.objects.all()
       
        if int(request.GET.get('search-sign', '0')) == 1:
            search_query = {
                'document_type':                    5,
                'name':                             request.GET.get('orders-on-others-search-number',''),
                'department':                       '',
                'period_from':                      request.GET.get('oom_search_from',''),
                'period_to':                        request.GET.get('oom_search_to',''),
                'orders_of_others_res_officier':    request.GET.get('oom_search_res', ''),
                'content':                          request.GET.get('orders-on-others-search-content', '')
             }
           
            orders = search(search_query)
            p_orders = Paginator(orders, 1000)
            page_number = request.GET.get('page', 1)

        
        else:
            orders = OrdersOnOtherMatters.objects.all().order_by('-id')
            p_orders = Paginator(orders, 20)
            page_number = request.GET.get('page', 1)
        
        page = p_orders.get_page(page_number)
        
        return render(request, 'reg_jounals/orders_on_others.html', context={'orders':page,'res_users':users})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OrderOnOtherMatters(request):
    if request.user.is_authenticated:
        order_form = OrdersOnOtherMatters_form()
        orders = OrdersOnOtherMatters.objects.all()
        orders_count = len(orders)
        if orders_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[orders_count - 1].oom_number
            cut_symb = (len(str(order_prev_num)) - 2)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1
        if request.method == "POST":
            order_form =OrdersOnOtherMatters_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../orders_on_others/')


            else:
                return render(request, 'reg_jounals/no_auth.html')
        return render(request, 'reg_jounals/OrdersOnOtherMatters_add.html', context={'form':order_form, 'next_num':order_next_num_})

def upd_OrderOnOtherMatters(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            order = OrdersOnOtherMatters.objects.get(id__exact=id)
            bound_form = OrdersOnOtherMatters_form(instance=order)
            return render(request, 'reg_jounals/OrdersOnOtherMatters_upd.html', context={'form':bound_form, 'order':order})
        else:
            order = OrdersOnOtherMatters.objects.get(id__iexact=id)
            bound_form = OrdersOnOtherMatters_form(request.POST, instance=order)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/orders_on_others')

def del_OrderOnOtherMatters(request, id):
    if request.user.is_authenticated:
        order = OrdersOnOtherMatters.objects.get(id__iexact=id)
        order.delete()
        return redirect('/orders_on_others')

# Приказы на отпуск -----------------------
def order_on_vacation(request):
    if request.user.is_authenticated:

                orders = OrdersOnVacation.objects.all().order_by('-id')
                p_orders = Paginator(orders, 20)
                page_number = request.GET.get('page', 1)
                page = p_orders.get_page(page_number)
                count = len(orders)
                return render(request, 'reg_jounals/orders_on_vacation.html', context={'orders':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OrderOnVacation(request):
    if request.user.is_authenticated:
        order_form = OrdersOnVacation_form()
        depts = Departments.objects.all()
        orders = OrdersOnVacation.objects.all()
        orders_count = len(orders)
        if orders_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[orders_count - 1].oov_number
            cut_symb = (len(str(order_prev_num)) - 5)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        if request.method == "POST":
            order_form =OrdersOnVacation_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../orders_on_vacation/')


    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/OrdersOnVacation_add.html', context={'form':order_form, 'depts':depts, 'next_num':order_next_num_})

def upd_OrderOnVacation(request, id):
    if request.user.is_authenticated:
        depts = Departments.objects.all()
        if request.method == "GET":
            order = OrdersOnVacation.objects.get(id__iexact=id)
            bound_form = OrdersOnVacation_form(instance=order)
            return render(request, 'reg_jounals/OrdersOnVacation_upd.html', context={'form':bound_form, 'order':order, 'depts':depts})
        else:
            order = OrdersOnVacation.objects.get(id__iexact=id)
            bound_form = OrdersOnVacation_form(request.POST, instance=order)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/orders_on_vacation')

def del_OrderOnVacation(request, id):
    if request.user.is_authenticated:
        order = OrdersOnVacation.objects.get(id__iexact=id)
        order.delete()
        return redirect('/orders_on_vacation')

# Приказы о командировках -----------------
def order_of_BTrip(request):
    if request.user.is_authenticated:
        deps = Departments.objects.filter(is_aup=0).filter(notused=0)
        
        search_query = {
            'document_type':    2,
            'name':             request.GET.get('bt_search', ''),
            'destination':      request.GET.get('orders-of-buisness-trip-search-destination',''),
            'period_from':      request.GET.get('orders-of-buisness-trip-search-from',''),
            'period_to':        request.GET.get('orders-of-buisness-trip-search-to',''),
            'department':       request.GET.get('bt_search_dep','')
        }
       
        if int(request.GET.get('search-sign', '0')) == 1:
            orders = search(search_query)
            p_orders = Paginator(orders, 1000)
            page_number = request.GET.get('page',1)

        else:
            orders = OrdersOfBTrip.objects.all().order_by('-bt_date', '-id')
            p_orders = Paginator(orders, 20)
            page_number = request.GET.get('page', 1)

        page = p_orders.get_page(page_number)
        count = len(orders)
        return render(request, 'reg_jounals/orders_of_BTrip.html', context={'orders':page, 'count':count, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OrderOfBTrip(request):
    if request.user.is_authenticated:
        order_form = OrdersOfBTrip_form()
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        orders = OrdersOfBTrip.objects.all()
        order_count = len(orders)
        if order_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[order_count - 1].bt_number
            cut_symb = (len(str(order_prev_num)) - 1)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        if request.method == "POST":
            order_form      = OrdersOfBTrip_form(request.POST)
            
            bound_employer  = request.POST.get('order-of-btrip-bound-employer-field',   '')
            department      = request.POST.get('order-of-btrip-department',             '')  

            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_, bound_employer, department)
                return redirect('../orders_of_BTrip/')

    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/OrdersOfBTrip_add.html', context={'form':order_form, 'deps':deps, 'next_num':order_next_num_})

def get_ordersBtrip(request):
    if request.user.is_authenticated:
        orders = OrdersOfBTrip.objects.values('id', 'bt_date', 'bt_place', 'bt_number', 'bt_emloyer', 'bt_res_officer', 'bt_dep__dep_name')
        orders = list(orders)
        return JsonResponse(orders, safe=False)

def upd_OrderOfBTrip(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            deps = TDep.objects.filter(notused=0).filter(is_aup=0)
            order = OrdersOfBTrip.objects.get(id=id)
            bound_form = OrdersOfBTrip_form(instance=order)
            return render(request, 'reg_jounals/OrdersOfBTrip_upd.html', context={'form':bound_form, 'order':order, 'deps':deps})
        else:
            order = OrdersOfBTrip.objects.get(id=id)
            bound_form = OrdersOfBTrip_form(request.POST, instance=order)

            updated_bound_employer  = request.POST.get('order-of-btrip-bound-employer-field',   '')
            updated_department      = request.POST.get('order-of-btrip-department',             '')

            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()

                if new_obj.bound_employer_id != updated_bound_employer:
                    new_obj.bound_employer = get_employer_from_db(updated_bound_employer)
                    new_obj.save()
                
                if new_obj.department != updated_department:
                    new_obj.department = get_department_from_db(updated_department)
                    new_obj.save()                   

                return redirect('/orders_of_BTrip')


            else:
                return render(request, 'reg_jounals/no_auth.html')
        return render(request, 'reg_jounals/OrdersOfBTrip_add.html', context={'form':order_form})

def del_OrderOfBTrip(request, id):
    if request.user.is_authenticated:
        order = OrdersOfBTrip.objects.get(id__iexact=id)
        order.delete()
        return redirect('/orders_of_BTrip')

# Приказы по личному составу ----------------
def order_on_personnel(request):
    if request.user.is_authenticated:
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        events = OrdersOnPersonnelTypes.objects.all()
        
        if int(request.GET.get('search-sign', '0')) == 1:
            search_query = {
                'document_type':                7,
                'orders_on_personnel_number':   request.GET.get('orders-on-personnel-search-number', ''),
                'name':                         request.GET.get('op_search', ''),
                'content':                      request.GET.get('orders-on-personnel-search-content',''),
                'orders_on_personnel_event':    request.GET.get('op_event', ''),
                'period_from':                  request.GET.get('op_search_from',''),
                'period_to':                    request.GET.get('op_search_to',''),
                'department':                   request.GET.get('orders-on-personnel-search-department','')
            }
       
        
            orders = search(search_query)
            p_orders = Paginator(orders, 1000)
            page_number = request.GET.get('page', 1)
        else:
            orders = OrdersOnPersonnel.objects.all().order_by('-id')
            p_orders = Paginator(orders, 20)
            page_number = request.GET.get('page', 1)
        
        page = p_orders.get_page(page_number)
        return render(request, 'reg_jounals/orders_on_personnel.html', context={'orders':page,'events':events, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OrderOnPersonnel(request):
    if request.user.is_authenticated:
        tab_deps        = TDep.objects.all().filter(is_aup=0)
        tab_subdeps     = TDep.objects.filter(is_aup=1)
        tab_pos         = TPos.objects.all()
        order_form      = OrdersOnPersonnel_form()
        depts           = Departments.objects.all()
        orders          = OrdersOnPersonnel.objects.all().order_by('id')

        order_count = len(orders)
        if order_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[order_count - 1].op_number
            cut_symb = (len(str(order_prev_num)) - 2)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        if request.method == "POST":
            
            bound_employer  = request.POST.get('order-of-personell-bound-employer-field', '')
            department      = request.POST.get('dep_for_tabel','')
            no_department   = request.POST.get('order-of-personnel-no-department', '')
            no_employer     = request.POST.get('order-of-personnel-no-employer', '')

            if no_department:
                department = ''
                bound_employer = ''
            
            if no_employer:
                bound_employer = ''
           
            emp_info = {
                'fullname':         request.POST.get('short_fio',''),
                'position':         request.POST.get('tab_pos',''),
                'department':       department,
                'sub_department':   request.POST.get('subdep_for_tabel',''),
                'level':            request.POST.get('tab_level',''),
                'payment_level':    request.POST.get('tab_payment',''),
                'shift':            request.POST.get('tab_work', ''),
                'sex':              request.POST.get('tab_sex','')  

            }
   
            order_form = OrdersOnPersonnel_form(request.POST)
            if order_form.is_valid():
                user_       = request.user.first_name
                new_order   = order_form.saveFirst(user_, bound_employer, department)
                

                if emp_info['fullname'] and emp_info['position'] and emp_info['department'] and emp_info['level'] and emp_info['payment_level'] and emp_info['shift']:

                    
                    new_emp = create_or_update_employer(request, 0,emp_info)

                    if new_emp:
                        new_order.bound_employer = new_emp
                        new_order.save()


                return redirect('../orders_on_personnel/')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/OrdersOnPersonnel_add.html', context={'form':order_form, 'depts':depts, 'next_num':order_next_num_, 'tab_deps':tab_deps, 'tab_subdeps':tab_subdeps, 'tab_pos':tab_pos})

def upd_OrderOnPersonnel(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            order = OrdersOnPersonnel.objects.get(id__iexact=id)
            bound_form = OrdersOnPersonnel_form(instance=order)
            bound_employer = order.bound_employer
            deps = TDep.objects.filter(notused=0)
            positions = TPos.objects.all().order_by('name')
            return render(request, 'reg_jounals/OrdersOnPersonnel_upd.html', context={'form':bound_form, 'order':order, 'employer':bound_employer, 'tab_deps':deps.filter(is_aup=0), 'tab_subdeps':deps.filter(is_aup=1), 'tab_pos':positions})
        else:
            order = OrdersOnPersonnel.objects.get(id__iexact=id)
            bound_form = OrdersOnPersonnel_form(request.POST, instance=order)

            updated_bound_employer  = request.POST.get('order-of-personell-bound-employer-field','')
            updated_department      = request.POST.get('dep_for_tabel', '')

            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                
                if new_obj.bound_employer_id != updated_bound_employer:
                    if updated_bound_employer:
                        new_obj.bound_employer = TEmps.objects.get(id=updated_bound_employer)
                    else:
                        new_obj.bound_employer = None
                    new_obj.save()
               
                if new_obj.department_id != updated_department:
                    if updated_department:
                        new_obj.department_id = TDep.objects.get(id=updated_department)
                    else:
                        new_obj.department_id = None
                    new_obj.save()
                


                if order.bound_employer and order.op_type == 1:
                    # Обновить информацию о работнике в приказе
                    emp_info = {
                    'fullname':         request.POST.get('short_fio',''),
                    'position':         request.POST.get('tab_pos',''),
                    'department':       request.POST.get('dep_for_tabel',''),
                    'sub_department':   request.POST.get('subdep_for_tabel',''),
                    'level':            request.POST.get('tab_level',''),
                    'payment_level':    request.POST.get('tab_payment',''),
                    'shift':            request.POST.get('tab_work', ''),
                    'sex':              request.POST.get('tab_sex','')  

                    }

                    if emp_info['fullname'] and emp_info['position'] and emp_info['department'] and emp_info['level'] and emp_info['payment_level'] and emp_info['shift']:
                        create_or_update_employer(order.bound_employer_id,emp_info)
                
                return redirect('/orders_on_personnel')
            else:
                ers = bound_form.errors.as_data()

                for e in ers.keys():
                    print(str(e) + ' ' + str(ers.get(e)))
                return render(request, 'reg_jounals/OrdersOnPersonnel_upd.html', context={'form':bound_form, 'order':order})



def del_OrderOnPersonnel(request, id):
    if request.user.is_authenticated:
        order = OrdersOnPersonnel.objects.get(id__iexact=id)
        order.delete()
        return redirect('/orders_on_personnel')

# Трудовые договоры ---------------------------
def LaborContracts(request):
    if request.user.is_authenticated:
      

        if int(request.GET.get('search-sign', '0')) == 1:
            search_query = {
            'document_type':    8,
            'name':             request.GET.get('labor-contract-search-fio', ''),
            'period_from':      request.GET.get('dur-from',''),
            'period_to':        request.GET.get('dur-to',''),
            'department':       request.GET.get('lc_search','')
            }
       
            contracts = search(search_query)
            p_orders = Paginator(contracts, 1000)
            page_number = request.GET.get('page', 1)
        else:
            contracts = LaborContract.objects.all().order_by('-id')
            p_orders = Paginator(contracts, 20)
            page_number = request.GET.get('page', 1)
       
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        page = p_orders.get_page(page_number)

        return render(request, 'reg_jounals/laborContracts.html', context={'orders':page,'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_LaborContract(request):
    if request.user.is_authenticated:
        pos = TPos.objects.all()
        order_form = LaborContract_form()
        deps = TDep.objects.filter(is_aup=0).filter(notused=0)
        orders = LaborContract.objects.all()
        year_ = str(DT.date.today().year)
        year_ = year_[2:]
        orders_count = len(orders)
        
        if orders_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[orders_count - 1].lc_number
            cut_symb = (len(str(order_prev_num)) - 4)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1
        
        if request.method == "POST":
            
            bound_employer      = get_employer_from_db(request.POST.get('labor-contract-employer-field', ''))
            department          = get_department_from_db(request.POST.get('labor-contract-department-field', ''))
            position            = get_position_from_db(request.POST.get('sel_pos', ''))  

            order_form = LaborContract_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_, year_, bound_employer, department, position)
                return redirect('../laborContracts/')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/LaborContract_add.html', context={'form':order_form, 'deps':deps, 'next_num':order_next_num_, 'year_':year_, 'pos':pos})

def upd_LaborContract(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            deps = TDep.objects.filter(is_aup=0).filter(notused=0)
            pos = TPos.objects.all()
            order = LaborContract.objects.get(id__iexact=id)
            bound_form = LaborContract_form(instance=order)
            return render(request, 'reg_jounals/LaborContract_upd.html', context={'form':bound_form, 'order':order, 'pos':pos, 'deps':deps})
        else:

            updated_bound_employer  = get_employer_from_db(request.POST.get('labor-contract-employer-field',''))
            updated_department      = get_department_from_db(request.POST.get('labor-contract-department-field',''))
            updated_position       = get_position_from_db(request.POST.get('sel_pos', ''))

            order = LaborContract.objects.get(id__iexact=id)
            bound_form = LaborContract_form(request.POST, instance=order)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                
                if updated_bound_employer != new_obj.bound_employer:
                    new_obj.bound_employer = updated_bound_employer
                    new_obj.save()
                
                if updated_department != new_obj.department:
                    new_obj.department  =  updated_department
                    new_obj.save()
                
                if updated_position != new_obj.position:
                    new_obj.position = updated_position
                    new_obj.save()


                return redirect('/laborContracts')

def del_LaborContract(request, id):
    if request.user.is_authenticated:
        order = LaborContract.objects.get(id__iexact=id)
        order.delete()
        return redirect('/laborContracts')

# Трудовые книжки -------------------------------
def employment_history(request):
    if request.user.is_authenticated:
       
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)

        search_query = {
            'document_type':                4,
            'name':                         request.GET.get('eh_search', ''),
            'employment_history_type':      request.GET.get('eh_search_type',''),
            'period_from':                  request.GET.get('employment-history-search-date-invite-from',''),
            'period_to':                    request.GET.get('employment-history-search-date-invite-to',''),
            'department':                   request.GET.get('employment-history-search-department','')
        }
       
        if int(request.GET.get('search-sign', '0')) == 1:
            histories = search(search_query)
            p_orders = Paginator(histories, 1000)
            page_number = request.GET.get('page', 1)
            page = p_orders.get_page(page_number)
        else:
            histories = EmploymentHistory.objects.all().order_by('-eh_dateOfInv')
            p_orders = Paginator(histories, 10)
            page_number = request.GET.get('page', 1)
            page = p_orders.get_page(page_number)

        return render(request, 'reg_jounals/employment_history.html', context={'histories':page, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_EmploymentHistory(request):
    if request.user.is_authenticated:
        pos = TPos.objects.all()
        history_form = EmploymentHistory_form()
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        if request.method == "POST":
            history_form = EmploymentHistory_form(request.POST)

            department = get_department_from_db(request.POST.get('employment-history-department-field', ''))
            
            if history_form.is_valid():
                user_ = request.user.first_name
                history_form.saveFirst(user_, department)
                return redirect('../employment_history/')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/EmploymentHistory_add.html', context={'form':history_form, 'deps':deps, 'pos':pos})

def upd_EmploymentHistory(request, id):
    if request.user.is_authenticated:
        pos = TPos.objects.all()
        history = EmploymentHistory.objects.get(id__iexact=id)
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        
        if request.method == "GET":
           
            bound_form = EmploymentHistory_form(instance=history)
            return render(request, 'reg_jounals/EmploymentHistory_upd.html', context={'form':bound_form, 'history':history, 'deps':deps})
        else:
            
            updated_department = get_department_from_db(request.POST.get('employment-history-department-field', ''))

            bound_form = EmploymentHistory_form(request.POST, instance=history)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()

                if updated_department != new_obj.department:
                    new_obj.department = updated_department
                    new_obj.save()

                return redirect('/employment_history')

def del_EmploymentHistory(request, id):
    if request.user.is_authenticated:
        history = EmploymentHistory.objects.get(id__iexact=id)
        history.delete()
        return redirect('/employment_history')

def print_EmploymentHistory(request, id):
    if request.user.is_authenticated:
            history = EmploymentHistory.objects.get(id__iexact=id)
            return render(request, 'reg_jounals/EmploymentHistory_print.html', context={'history':history})

# Реестры больничных --------------------------------
def sick_regs(request):
    if request.user.is_authenticated:
        sick_docs = ""
        regs = ""
        deps = Departments.objects.all()
        search_query = request.GET.get('sd_search','')
        sq_dep = request.GET.get('sd_dep_search','')
        if search_query:
            sick_docs = SickDocument.objects.filter(sd_emp__icontains=search_query).order_by('-id')
            sdocs_count = len(sick_docs)
            return render(request, 'reg_jounals/sick_search.html', context={'sick_docs':sick_docs, 'search_query':search_query, 'sdocs_count':sdocs_count, 'deps':deps})
        else:
            if sq_dep:
                sick_docs = SickDocument.objects.filter(sd_dep=sq_dep).order_by('-id')
                sdocs_count = len(sick_docs)
                return render(request, 'reg_jounals/sick_search.html', context={'sick_docs':sick_docs, 'search_query':sq_dep, 'sdocs_count':sdocs_count, 'deps':deps})
            else:
                regs = SickRegistry.objects.all().order_by('-id')
                p_regs = Paginator(regs, 30)
                page_number = request.GET.get('page', 1)
                page = p_regs.get_page(page_number)
                return render(request, 'reg_jounals/sick_regs.html', context={'regs':page, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def create_SickRegistry(request, id):
    if request.user.is_authenticated:
        reg = SickRegistry.objects.get(id=id)
        positions = SickDocument.objects.filter(sd_bound_reg_id=id)

        count = len(positions)
        return render(request, 'reg_jounals/sick_reg_create.html', context={'positions':positions, 'year':reg.sr_year, 'rnum':reg.sr_number, 'reg':reg, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def add_SickRegistry(request):
    if request.user.is_authenticated:
        reg_form = SickRegistry_form()
        regs = SickRegistry.objects.all().order_by('sr_number')
        user_ = request.user.first_name
        year_ = DT.datetime.today().year
        reg_form.saveFirst(user_, year_)
        new_reg = last_doc(SickRegistry)


    else:
        return render(request, 'reg_jounals/no_auth.html')
    return redirect('/sick_reg/' + str(new_reg.id) + '/create')

def add_SickDocument(request, id):
    if request.user.is_authenticated:
        reg = SickRegistry.objects.get(id=id)
        doc_form = SickDocument_form()
        errs = doc_form.errors.as_data()
        if request.method == "POST":
            doc_form = SickDocument_form(request.POST)
            if doc_form.is_valid():
                user_ = request.user.first_name
                doc_form.saveFirst(user_, id)
                loc = '/sick_reg/'+str(id)+'/create/'
                return redirect(loc)
            else:
                errs = doc_form.errors.as_data()


                if errs['sd_number']:
                    dual_num = request.POST.get('sd_number','')
                    find_doc = SickDocument.objects.get(sd_number=dual_num)
                    print('yes')
                    errs = "Больничный лист c таким номером существует в реестре № " + str(find_doc.sd_bound_reg.sr_number) + " сотрудник: " + str(find_doc.sd_emp)
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/SickDocument_add.html', context={'form':doc_form, 'reg_num':str(reg.sr_number), 'errs':errs})

def upd_SickDocument(request, id):
    if request.user.is_authenticated:
        document = SickDocument.objects.get(id__exact=id)
        reg = SickRegistry.objects.get(id=document.sd_bound_reg_id)
        b_reg = document.sd_bound_reg_id
        if request.method == "GET":
            bound_form = SickDocument_form(instance=document)
            return render(request, 'reg_jounals/SickDocument_upd.html', context={'form':bound_form, 'document':document, 'b_reg':reg})
        else:
            document = SickDocument.objects.get(id__exact=id)
            bound_form = SickDocument_form(request.POST, instance=document)
            if bound_form.is_valid():
                user_ = request.user.first_name
                bound_form.save()
                loc = '/sick_reg/'+str(b_reg)+'/create/'
                return redirect(loc)

def ItemDel_SickList(request, id):
    if request.user.is_authenticated:
        item = SickDocument.objects.get(id__iexact=id)
        num = item.sd_bound_reg_id
        dest = '/sick_reg/' + str(num) + '/create/'
        item.delete()
        return redirect(dest)

def check_SickDocument(request, num):
    if request.user.is_authenticated:
        sdoc = SickDocument.objects.filter(sd_number__exact=num)
        print(sdoc)
        if sdoc:
            message = "Болничный лист с таким номером уже занесен в реестр № " + str(sdoc[0].sd_bound_reg.sr_number) + ". Сотрудник: " + str(sdoc[0].sd_emp)
        else:
            message = "Б\Л с таким номером не заносился в систему"
        return JsonResponse(message, safe=False)
# Приказы на отпуск новые ----------------------------

def new_order_on_vacation(request):
    if request.user.is_authenticated:
        items = ""
        orders = []
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)

        
        if int(request.GET.get('search-sign', '0')) == 1:
            search_query = {
                'document_type': 1,
                'name':request.GET.get('vac_search', ''),
                'vacation_type':request.GET.get('orders-of-vacation-search-type', ''),
                'period_from':request.GET.get('orders-of-vacation-search-date-from','0001-01-01'),
                'period_to':request.GET.get('orders-of-vacation-search-date-to', '3999-12-31'),
                'department':request.GET.get('vac_dep_search','')
            }

            page = search(search_query)
            return render(request, 'reg_jounals/vac_search.html', context={'items':page, 'search_query':search_query['name']})
        else:
            orders = NewOrdersOnVacation.objects.all().order_by('-id')
            p_orders = Paginator(orders, 20)
            page_number = request.GET.get('page', 1)
            page = p_orders.get_page(page_number)
            
        
            return render(request, 'reg_jounals/orders_on_vacation_new.html', context={'orders':page, 'deps':deps})
      
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_new_order_on_vacation(request):
    if request.user.is_authenticated:
        order_form = NewOrdersOnVacation_form()

        # Нумерация ----------------------------------------
        last_order = NewOrdersOnVacation.objects.latest('id')
        last_order_num = last_order.order_number
        cut_symb = (len(str(last_order_num)) - 6)
        next_num = int(last_order_num[:cut_symb]) + 1
        next_num = str(next_num) + '-К-ОТП'
        # --------------------------------------------------

        if request.method == "POST":
            order_form = NewOrdersOnVacation_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name

                order_form.saveFirst(user_)
                return redirect('/orders_on_vacation_new')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/OrdersOnVacation_new_add.html', context={'form':order_form, 'next_num':next_num})

def create_new_order_on_vacation(request, id):
    if request.user.is_authenticated:
        items = NewOrdersOnVacation_item.objects.filter(bound_order__exact=id).order_by('fio')
        order = NewOrdersOnVacation.objects.get(id=id)
        items_count = len(items)
        return render(request, 'reg_jounals/OrderOnVacation_new_create.html', context={'items':items, 'order':order, 'count':items_count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def new_order_on_vacation_addItem(request, order_id):
    if request.user.is_authenticated:
        item_form = NewOrdersOnVacationItem_form()
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        
        if request.method == "POST":
            item_form = NewOrdersOnVacationItem_form(request.POST)
            
            bound_employer  = get_employer_from_db(request.POST.get('vacation-item-employer-field',''))
            department      = get_department_from_db(request.POST.get('vacation-item-department-field',''))
            
            if item_form.is_valid():
                user_ = request.user.first_name
                print(order_id)
                item_form.saveFirst(order_id, user_, bound_employer, department)
                loc = '/orders_on_vacation_new/'+str(order_id)+'/create'
                return redirect(loc)
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/NewOrderOnVacation_addItem.html', context={'form':item_form, 'deps':deps, 'order_id':order_id})

def new_order_on_vacation_updItem(request, id):
    if request.user.is_authenticated:
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        item = NewOrdersOnVacation_item.objects.get(id__exact=id)
        if request.method == "GET":
            bound_form = NewOrdersOnVacationItem_form(instance=item)
            return render(request, 'reg_jounals/NewOrderOnVacation_updItem.html', context={'form':bound_form, 'item':item, 'deps':deps })
        else:
            item = NewOrdersOnVacation_item.objects.get(id__iexact=id)
            bound_form = NewOrdersOnVacationItem_form(request.POST, instance=item)
            
            updated_bound_employer  = get_employer_from_db(request.POST.get('vacation-item-employer-field',''))
            updated_department      = get_department_from_db(request.POST.get('vacation-item-department-field',''))
            
            if bound_form.is_valid():
                user_   = request.user.first_name
                new_obj = bound_form.save()

                if updated_bound_employer != new_obj.bound_employer:
                    new_obj.bound_employer = updated_bound_employer
                    new_obj.save()
                
                if updated_department != new_obj.department_new:
                    new_obj.department_new = updated_department
                    new_obj.save()

                loc = '/orders_on_vacation_new/'+str(item.bound_order.id)+'/create'
                return redirect(loc)

def new_order_on_vacation_delItem(request, id):
    if request.user.is_authenticated:
        item = NewOrdersOnVacation_item.objects.get(id__exact=id)


        dest = '/orders_on_vacation_new/' + str(item.bound_order.id) + '/create'
        item.delete()
        return redirect(dest)

def new_order_on_vacation_del(request, id):
    if request.user.is_authenticated:
        order = NewOrdersOnVacation.objects.get(id=id)
        items = NewOrdersOnVacation_item.objects.filter(bound_order=id)
        order.delete()
        items.delete()
        return redirect('/orders_on_vacation_new/')

# УДОСТОВЕРЕНИЯ ---------------------------------------------------

def identitys(request):
    if request.user.is_authenticated:
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        search_query = request.GET.get('ident_search','')
        sq_dep = request.GET.get('ident_dep_search','')
    
        if int(request.GET.get('search-sign', '0')) == 1:
            search_query = {
                'document_type':    10,
                'name':             request.GET.get('ident_search', ''),
                'period_from':      request.GET.get('identity-search-date-from',''),
                'period_to':        request.GET.get('identity-search-date-to',''),
                'department':       request.GET.get('ident_dep_search','')
            }
            ident = search(search_query)
            p_ident = Paginator(ident, 1000)
            page_number = request.GET.get('page', 1)
  
        else:
            ident = Identity.objects.all().order_by('-id')
            p_ident = Paginator(ident, 20)
            page_number = request.GET.get('page', 1)
        
        page = p_ident.get_page(page_number)

        return render(request, 'reg_jounals/identitys.html', context={'idents':page, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_identitys(request):
    if request.user.is_authenticated:
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        ident_form = Identity_form()
        next_num = int(Identity.objects.latest('id').number) + 1
        if request.method == "POST":
            ident_form = Identity_form(request.POST)
            if ident_form.is_valid():
                bound_employer  = get_employer_from_db(request.POST.get('identity-employer-field'))
                department      = get_department_from_db(request.POST.get('identity-department-field'))
                user_ = request.user.first_name
                ident_form.saveFirst(user_, bound_employer, department)
                return redirect('/identity')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/identity_add.html', context={'form':ident_form, 'next_num':next_num, 'deps':deps})

def upd_identitys(request, id):
    if request.user.is_authenticated:
        ident = Identity.objects.get(id__iexact=id)
        deps = TDep.objects.filter(notused=0).filter(is_aup=0)
        if request.method == "GET":
            
            bound_form = Identity_form(instance=ident)
            return render(request, 'reg_jounals/identity_upd.html', context={'form':bound_form, 'ident':ident, 'deps':deps})
        else:
        
            bound_form = Identity_form(request.POST, instance=ident)
            if bound_form.is_valid():
                updated_bound_employer  = get_employer_from_db(request.POST.get('identity-employer-field'))
                updated_department      = get_department_from_db(request.POST.get('identity-department-field'))
                user_ = request.user.first_name
                new_obj = bound_form.save()
                
                if updated_bound_employer != new_obj.bound_employer:
                    new_obj.bound_employer = updated_bound_employer
                    new_obj.save()
                
                if updated_department != new_obj.department_new:
                    new_obj.department_new = updated_department
                    new_obj.save()

                return redirect('/identity')

def del_identitys(request, id):
    if request.user.is_authenticated:
        ident = Identity.objects.get(id__exact=id)


        dest = '/identity'
        ident.delete()
        return redirect(dest)

# ЛОГИ -------------------------------------------------------------
def logs_(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dfrom = request.POST.get('l_date_from', '')
            dto = request.POST.get('l_date_to', '')
            user = request.POST.get('l_user', '')
            if user:
                logs_ = logs.objects.filter(date__range=(dfrom,dto)).filter(res_officer=user)
            else:
                logs_ = logs.objects.filter(date__range=(dfrom,dto))
            pag = 999
        else:
            pag = 20
            logs_ = logs.objects.all()
        users = User.objects.all().order_by('first_name')
        p_logs = Paginator(logs_, pag)
        page_number = request.GET.get('page', 1)
        page = p_logs.get_page(page_number)
        return render(request, 'reg_jounals/log.html', context={'logs':page, 'users':users})
# ОТЧЕТЫ -----------------------------------------------------------
def reports(request):
    if request.user.is_authenticated:
        deps = Departments.objects.all()
        if request.method == 'POST':
            employer = request.POST.get('reports-emp', '')
            dep = request.POST.get('reports-dep','')
            event = request.POST.get('reports-event','')
            type = request.POST.get('reports-type', '')
            dfrom = request.POST.get('reports-from')
            dto = request.POST.get('reports-to')
            print(employer + '\n' + type + '\n' + dfrom + '\n' + dto)
            # По сотруднику -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if type == '1':
                if employer and dfrom and dto:
                    vacantions = NewOrdersOnVacation_item.objects.all().filter(fio__icontains=employer, bound_order__order_date__range=(dfrom,dto))
                    personnel = OrdersOnPersonnel.objects.all().filter(op_emloyer__icontains=employer).filter(op_date__range=(dfrom,dto))
                    trips = OrdersOfBTrip.objects.all().filter(bt_emloyer__icontains=employer).filter(bt_date__range=(dfrom,dto))
                    contracts = LaborContract.objects.all().filter(lc_emloyer__icontains=employer).filter(lc_date__range=(dfrom,dto))
                    invite = LetterOfInvite.objects.all().filter(loi_employee__icontains=employer).filter(loi_date__range=(dfrom,dto))
                    resign = LetterOfResignation.objects.all().filter(lor_employee__icontains=employer).filter(lor_date__range=(dfrom,dto))
                    history = ""
                else:
                    if employer:
                        vacantions = NewOrdersOnVacation_item.objects.all().filter(fio__icontains=employer)
                        personnel = OrdersOnPersonnel.objects.all().filter(op_emloyer__icontains=employer)
                        trips = OrdersOfBTrip.objects.all().filter(bt_emloyer__icontains=employer)
                        contracts = LaborContract.objects.all().filter(lc_emloyer__icontains=employer)
                        invite = LetterOfInvite.objects.all().filter(loi_employee__icontains=employer)
                        resign = LetterOfResignation.objects.all().filter(lor_employee__icontains=employer)
                        history = EmploymentHistory.objects.all().filter(eh_employer__icontains=employer)
                # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                # По подразделению -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if type == '2':
                if dep and dfrom and dto:
                    vacantions = NewOrdersOnVacation_item.objects.all().filter(dep=dep, bound_order__order_date__range=(dfrom,dto))
                    personnel = OrdersOnPersonnel.objects.all().filter(op_dep=dep).filter(op_date__range=(dfrom,dto))
                    trips = OrdersOfBTrip.objects.all().filter(bt_dep=dep).filter(bt_date__range=(dfrom,dto))
                    contracts = LaborContract.objects.all().filter(lc_dep=dep).filter(lc_date__range=(dfrom,dto))
                    invite = LetterOfInvite.objects.all().filter(loi_department=dep).filter(loi_date__range=(dfrom,dto))
                    resign = LetterOfResignation.objects.all().filter(lor_departament=dep).filter(lor_date__range=(dfrom,dto))
                    history = " "
                else:
                    if dep:
                        vacantions = NewOrdersOnVacation_item.objects.all().filter(dep=dep)
                        personnel = OrdersOnPersonnel.objects.all().filter(op_dep=dep)
                        trips = OrdersOfBTrip.objects.all().filter(bt_dep=dep)
                        contracts = LaborContract.objects.all().filter(lc_dep=dep)
                        invite = LetterOfInvite.objects.all().filter(loi_department=dep)
                        resign = LetterOfResignation.objects.all().filter(lor_departament=dep)
                        history = EmploymentHistory.objects.all().filter(eh_dep=dep)
                # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                # По событию -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if type == '3':

                if event and dfrom and dto and dep:
                    if event == 'Прием на работу' or event == 'Увольнение' or event == 'Перевод' or event == 'Другое':
                        print(event)
                        vacantions = ''
                        personnel = OrdersOnPersonnel.objects.all().filter(op_dep=dep).filter(op_date__range=(dfrom,dto)).filter(op_type__name=event)
                        print(personnel)
                        trips = ''
                    else:
                        if event == 'Командировка':
                            trips = OrdersOfBTrip.objects.all().filter(bt_date__range=(dfrom,dto)).filter(bt_dep=dep)
                            personnel = ''
                            vacantions = ''
                        else:
                            if event == 'Отпуск':
                                trips = ''
                                personnel = ''
                                vacantions = NewOrdersOnVacation_item.objects.all().filter(dep=dep, bound_order__order_date__range=(dfrom,dto))

                    contracts = ''
                    invite = ''
                    resign = ''
                    history = ''

                else:
                    if event and dfrom and dto:
                        # print(event)
                        if event == 'Прием на работу' or event == 'Увольнение' or event == 'Перевод' or event == 'Другое':
                            personnel = OrdersOnPersonnel.objects.all().filter(op_date__range=(dfrom,dto)).filter(op_type__name=event)
                            trips = ''
                            vacantions = ''
                        else:
                            if event == 'Командировка':
                                trips = OrdersOfBTrip.objects.all().filter(bt_date__range=(dfrom,dto))
                                personnel = ''
                                vacantions = ''
                            else:
                                if event == 'Отпуск':
                                    vacantions = NewOrdersOnVacation_item.objects.all().filter(bound_order__order_date__range=(dfrom,dto))
                                    trips = ''
                                    personnel = ''
                        contracts = ''
                        invite = ''
                        resign = ''
                        history = ''

                    else:
                        if event:
                            # print(event)
                            if event == 'Прием на работу' or event == 'Увольнение' or event == 'Перевод' or event == 'Другое':
                                personnel = OrdersOnPersonnel.objects.all().filter(op_type__name=event)
                                trips = ''
                                vacantions = ''
                            else:
                                if event == 'Командировка':
                                    trips = OrdersOfBTrip.objects.all()
                                    personnel = ''
                                    vacantions = ''
                                else:
                                    if event == 'Отпуск':
                                        vacantions = NewOrdersOnVacation_item.objects.all()
                                        trips = ''
                                        personnel = ''
                            contracts = ''
                            invite = ''
                            resign = ''
                            history = ''
                # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            return render(request, 'reg_jounals/reports.html', context={'history':history, 'resign':resign, 'vacantions':vacantions, 'personnel':personnel, 'trips':trips, 'contracts':contracts, 'invite':invite, 'deps':deps})

        else:
            return render(request, 'reg_jounals/reports.html', context={'deps':deps})

# @login_required        
def invite_checkin(request):
    message = 'standby'
    if request.method == 'POST':
    
        dinvite = request.POST.get('checkinDate', '')
        citizen = request.POST.get('citizen', '')  

        new_record = inviteCheckin_model.objects.create(
            checkinDate =  dinvite,
            citizen = citizen
        )
  

        if new_record.pk:
            message = "Запись создана" + str(new_record.checkinDate)
        else:
            message = "Ошибка"
    return redirect('/')

def invite_checkin_cancel(request, id):
    record = inviteCheckin_model.objects.get(id=id)

    if record.cancelled == 0:
        record.cancelled = 1
        record.save()
        message = "Запись отменена"
    else:
        record.cancelled = 0
        record.save()
        message = "Запись возобновлена"
    return JsonResponse(message, safe=False)



def invite_checkin_get(request, count):
    if count == 0:
        records = inviteCheckin_model.objects.filter(cancelled=False).order_by('-checkinDate').values()
    else:
        records = inviteCheckin_model.objects.filter(cancelled = 0).filter(checkinDate__gte = DT.datetime.now()).order_by('-checkinDate').values()[:count]

    records = list(records)
    
    return JsonResponse(records, safe=False)
