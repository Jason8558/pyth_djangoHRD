from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
import datetime as DT
from itertools import groupby

page_count = 15

def index(request):
    if request.user.is_authenticated:

        return render(request, 'reg_jounals/index.html')

    else: return redirect('/accounts/login/')

def logfile(request):
    if request.user.is_authenticated:
        logfile = open('log.txt')
        log = []
        for line in logfile:
            log.append(line)
    return render(request, 'reg_jounals/log.html', context={'log':log})


def outbound_docs(request):
    if request.user.is_authenticated:
        auth = request.user.is_authenticated
        date_from = request.GET.get('doc_search_from','')
        date_to = request.GET.get('doc_search_to', '')
        if date_from and date_to:
            date_from = DT.datetime.strptime(date_from, '%d.%m.%Y').date()
            date_to = DT.datetime.strptime(date_to, '%d.%m.%Y').date()
            documents = OutBoundDocument.objects.filter(doc_date__range=(date_from, date_to)).order_by('doc_date')
        else:
            documents = OutBoundDocument.objects.all().order_by('-id')
        p_documents = Paginator(documents, 15)
        page_number = request.GET.get('page', 1)
        page = p_documents.get_page(page_number)
        count = len(documents)
        method = str(request.method)
        usr = str(request.user.first_name)
        i = 0
        return render(request, 'reg_jounals/outbound_docs.html', context={'documents':page, 'count':count, 'auth':auth, 'i':i})
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
                return redirect('/journals/outbound_docs/')

def del_OutBoundDocument(request, id):
    if request.user.is_authenticated:
        document = OutBoundDocument.objects.get(id__iexact=id)
        document.delete()
        return redirect('/journals/outbound_docs/')



def letter_of_resignation(request):
    if request.user.is_authenticated:
        search_query = request.GET.get('lor_search','')
        if search_query:
            letters = LetterOfResignation.objects.filter(lor_employee__icontains=search_query)
        else:
            letters = LetterOfResignation.objects.all().order_by('-id')
        count = len(letters)
        p_letters = Paginator(letters, 10)
        page_number = request.GET.get('page', 1)
        page = p_letters.get_page(page_number)

        return render(request, 'reg_jounals/letters_of_resignation.html', context={'letters':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')


def nr_LetterOfResignation(request):
    if request.user.is_authenticated:
        letter_form = LetterOfResignation_form()
        depts = Departments.objects.all()
        letters = LetterOfResignation.objects.all()
        letters_count = len(letters)
        if letters_count == 0:
            letter_next_num_ = 1
        else:
            letter_prev_num = letters[letters_count - 1].lor_number
            letter_next_num_ = int(letter_prev_num) + 1
        if request.method == "POST":
            letter_form = LetterOfResignation_form(request.POST)
            if letter_form.is_valid():
                user_ = request.user.first_name
                letter_form.saveFirst(user_)
                return redirect('../letters_of_resignation/')
        else:

            return render(request, 'reg_jounals/LetterOfResignation_add.html', context={'form':letter_form, 'next_num':letter_next_num_})
    else:
        return render(request, 'reg_jounals/no_auth.html')





def upd_LetterOfResignation(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            letter = LetterOfResignation.objects.get(id__iexact=id)
            bound_form = LetterOfResignation_form(instance=letter)
            return render(request, 'reg_jounals/LetterOfResignation_upd.html', context={'form':bound_form, 'letter':letter})
        else:
            letter = LetterOfResignation.objects.get(id__iexact=id)
            bound_form = LetterOfResignation_form(request.POST, instance=letter)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/journals/letters_of_resignation')

def del_LetterOfResignation(request, id):
    if request.user.is_authenticated:
        letter = LetterOfResignation.objects.get(id__iexact=id)
        letter.delete()
        return redirect('/journals/letters_of_resignation')




def letter_of_invite(request):
        if request.user.is_authenticated:
            search_query = request.GET.get('loi_search','')
            if search_query:
                letters = LetterOfInvite.objects.filter(loi_employee__icontains=search_query)
            else:
                letters = LetterOfInvite.objects.all().order_by('-id')
            count = len(letters)

            p_letters = Paginator(letters, 10)
            page_number = request.GET.get('page', 1)
            page = p_letters.get_page(page_number)
            return render(request, 'reg_jounals/letters_of_invite.html', context={'letters':page, 'count':count})
        else:
            return render(request, 'reg_jounals/no_auth.html')

def upd_LetterOfInvite(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            letter = LetterOfInvite.objects.get(id__iexact=id)
            bound_form = LetterOfInvite_form(instance=letter)
            return render(request, 'reg_jounals/LetterOfInvite_upd.html', context={'form':bound_form, 'letter':letter})
        else:
            letter = LetterOfInvite.objects.get(id__iexact=id)
            bound_form = LetterOfInvite_form(request.POST, instance=letter)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/journals/letters_of_invite')

def nr_LetterOfInvite(request):
    if request.user.is_authenticated:
        letter_form = LetterOfInvite_form()
        depts = Departments.objects.all()
        letters = LetterOfInvite.objects.all()
        letters_count = len(letters)
        if letters_count == 0:
            letter_next_num_ = 1
        else:
            letter_prev_num = letters[letters_count - 1].loi_number
            letter_next_num_ = int(letter_prev_num) + 1
        if request.method == 'POST':
            letter_form = LetterOfInvite_form(request.POST)
            if letter_form.is_valid():
                user_ = request.user.first_name
                letter_form.saveFirst(user_)
                return redirect('../letters_of_invite/')
        return render(request, 'reg_jounals/LetterOfInvite_add.html', context={'form':letter_form, 'next_num':letter_next_num_})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def del_LetterOfInvite(request, id):
    if request.user.is_authenticated:
        letter = LetterOfInvite.objects.get(id__iexact=id)
        letter.delete()
        return redirect('/journals/letters_of_invite')

def order_other_matters(request):
    if request.user.is_authenticated:
        date_from = request.GET.get('oom_search_from','')
        date_to = request.GET.get('oom_search_to', '')
        if date_from and date_to:
            date_from = DT.datetime.strptime(date_from, '%d.%m.%Y').date()
            date_to = DT.datetime.strptime(date_to, '%d.%m.%Y').date()
            orders = OrdersOnOtherMatters.objects.filter(oom_date__range=(date_from, date_to)).order_by('oom_date')
        else:
            orders = OrdersOnOtherMatters.objects.all().order_by('-id')
        p_orders = Paginator(orders, 10)
        page_number = request.GET.get('page', 1)
        page = p_orders.get_page(page_number)
        count = len(orders)
        return render(request, 'reg_jounals/orders_on_others.html', context={'orders':page, 'count':count})
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
                return redirect('/journals/orders_on_others')

def del_OrderOnOtherMatters(request, id):
    if request.user.is_authenticated:
        order = OrdersOnOtherMatters.objects.get(id__iexact=id)
        order.delete()
        return redirect('/journals/orders_on_others')

def order_on_vacation(request):
    if request.user.is_authenticated:
        orders =OrdersOnVacation.objects.all().order_by('-id')
        p_orders = Paginator(orders, page_count)
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
                return redirect('/journals/orders_on_vacation')

def del_OrderOnVacation(request, id):
    if request.user.is_authenticated:
        order = OrdersOnVacation.objects.get(id__iexact=id)
        order.delete()
        return redirect('/journals/orders_on_vacation')


def order_of_BTrip(request):
    if request.user.is_authenticated:
        search_query = request.GET.get('bt_search','')
        if search_query:
            orders = OrdersOfBTrip.objects.filter(bt_emloyer__icontains=search_query)
        else:
            orders = OrdersOfBTrip.objects.all().order_by('-id')

        p_orders = Paginator(orders, page_count)
        page_number = request.GET.get('page', 1)
        page = p_orders.get_page(page_number)
        count = len(orders)
        return render(request, 'reg_jounals/orders_of_BTrip.html', context={'orders':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OrderOfBTrip(request):
    if request.user.is_authenticated:
        order_form = OrdersOfBTrip_form()
        depts = Departments.objects.all()
        orders = OrdersOfBTrip.objects.all()
        order_count = len(orders)
        if order_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[order_count - 1].bt_number
            cut_symb = (len(str(order_prev_num)) - 1)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        if request.method == "POST":
            order_form =OrdersOfBTrip_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../orders_of_BTrip/')

    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/OrdersOfBTrip_add.html', context={'form':order_form, 'depts':depts, 'next_num':order_next_num_})

def upd_OrderOfBTrip(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            order = OrdersOfBTrip.objects.get(id__iexact=id)
            bound_form = OrdersOfBTrip_form(instance=order)
            return render(request, 'reg_jounals/OrdersOfBTrip_upd.html', context={'form':bound_form, 'order':order})
        else:
            order = OrdersOfBTrip.objects.get(id__iexact=id)
            bound_form = OrdersOfBTrip_form(request.POST, instance=order)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/journals/orders_of_BTrip')


            else:
                return render(request, 'reg_jounals/no_auth.html')
        return render(request, 'reg_jounals/OrdersOfBTrip_add.html', context={'form':order_form})

def del_OrderOfBTrip(request, id):
    if request.user.is_authenticated:
        order = OrdersOfBTrip.objects.get(id__iexact=id)
        order.delete()
        return redirect('/journals/orders_of_BTrip')

def order_on_personnel(request):
    if request.user.is_authenticated:
        search_query = request.GET.get('op_search','')
        date_from = request.GET.get('op_search_from','')
        date_to = request.GET.get('op_search_to', '')
        if date_from and date_to:
            date_from = DT.datetime.strptime(date_from, '%d.%m.%Y').date()
            date_to = DT.datetime.strptime(date_to, '%d.%m.%Y').date()
            orders = OrdersOnPersonnel.objects.filter(op_date__range=(date_from, date_to)).order_by('op_date')
        else:
            if search_query:
                orders = OrdersOnPersonnel.objects.filter(op_emloyer__icontains=search_query).order_by('-id')
            else:
                orders = OrdersOnPersonnel.objects.all().order_by('-id')



        p_orders = Paginator(orders, page_count)
        page_number = request.GET.get('page', 1)
        page = p_orders.get_page(page_number)
        count = len(orders)
        return render(request, 'reg_jounals/orders_on_personnel.html', context={'orders':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OrderOnPersonnel(request):
    if request.user.is_authenticated:
        order_form = OrdersOnPersonnel_form()
        depts = Departments.objects.all()
        orders = OrdersOnPersonnel.objects.all().order_by('id')

        order_count = len(orders)
        if order_count == 0:
            order_next_num_ = 1
        else:
            order_prev_num = orders[order_count - 1].op_number
            cut_symb = (len(str(order_prev_num)) - 2)
            order_next_num_ = int(order_prev_num[:cut_symb]) + 1

        if request.method == "POST":
            order_form =OrdersOnPersonnel_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../orders_on_personnel/')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/OrdersOnPersonnel_add.html', context={'form':order_form, 'depts':depts, 'next_num':order_next_num_})


def upd_OrderOnPersonnel(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            order = OrdersOnPersonnel.objects.get(id__iexact=id)
            bound_form = OrdersOnPersonnel_form(instance=order)
            return render(request, 'reg_jounals/OrdersOnPersonnel_upd.html', context={'form':bound_form, 'order':order})
        else:
            order = OrdersOnPersonnel.objects.get(id__iexact=id)
            bound_form = OrdersOnPersonnel_form(request.POST, instance=order)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/journals/orders_on_personnel')

def del_OrderOnPersonnel(request, id):
    if request.user.is_authenticated:
        order = OrdersOnPersonnel.objects.get(id__iexact=id)
        order.delete()
        return redirect('/journals/orders_on_personnel')

def LaborContracts(request):
    if request.user.is_authenticated:
        search_query = request.GET.get('lc_search','')
        if search_query:
            contracts = LaborContract.objects.filter(lc_dep__dep_name__icontains=search_query)
        else:
            contracts = LaborContract.objects.all().order_by('-id')
        p_orders = Paginator(contracts, 10)
        page_number = request.GET.get('page', 1)
        page = p_orders.get_page(page_number)
        count = len(contracts)
        return render(request, 'reg_jounals/laborContracts.html', context={'orders':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_LaborContract(request):
    if request.user.is_authenticated:
        order_form = LaborContract_form()
        depts = Departments.objects.all()
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
            order_form = LaborContract_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_, year_)
                return redirect('../laborContracts/')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/LaborContract_add.html', context={'form':order_form, 'depts':depts, 'next_num':order_next_num_, 'year_':year_})

def upd_LaborContract(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            order = LaborContract.objects.get(id__iexact=id)
            bound_form = LaborContract_form(instance=order)
            return render(request, 'reg_jounals/LaborContract_upd.html', context={'form':bound_form, 'order':order})
        else:
            order = LaborContract.objects.get(id__iexact=id)
            bound_form = LaborContract_form(request.POST, instance=order)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/journals/laborContracts')

def del_LaborContract(request, id):
    if request.user.is_authenticated:
        order = LaborContract.objects.get(id__iexact=id)
        order.delete()
        return redirect('/journals/laborContracts')

def employment_history(request):
    if request.user.is_authenticated:

        search_query = request.GET.get('eh_search','')
        if search_query:
            histories = EmploymentHistory.objects.filter(eh_employer__icontains=search_query)
            print(histories)
        else:
            histories = EmploymentHistory.objects.all().order_by('-id')
        p_orders = Paginator(histories, page_count)
        page_number = request.GET.get('page', 1)
        page = p_orders.get_page(page_number)
        count = len(histories)
        return render(request, 'reg_jounals/employment_history.html', context={'histories':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_EmploymentHistory(request):
    if request.user.is_authenticated:
        history_form = EmploymentHistory_form()
        depts = Departments.objects.all()
        if request.method == "POST":
            history_form = EmploymentHistory_form(request.POST)
            if history_form.is_valid():
                user_ = request.user.first_name
                history_form.saveFirst(user_)
                return redirect('../employment_history/')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/EmploymentHistory_add.html', context={'form':history_form, 'depts':depts})

def upd_EmploymentHistory(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            history = EmploymentHistory.objects.get(id__iexact=id)
            bound_form = EmploymentHistory_form(instance=history)
            return render(request, 'reg_jounals/EmploymentHistory_upd.html', context={'form':bound_form, 'history':history})
        else:
            order = EmploymentHistory.objects.get(id__iexact=id)
            bound_form = EmploymentHistory_form(request.POST, instance=order)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/journals/employment_history')

def del_EmploymentHistory(request, id):
    if request.user.is_authenticated:
        history = EmploymentHistory.objects.get(id__iexact=id)
        history.delete()
        return redirect('/journals/employment_history')

def print_EmploymentHistory(request, id):
    if request.user.is_authenticated:
            history = EmploymentHistory.objects.get(id__iexact=id)
            return render(request, 'reg_jounals/EmploymentHistory_print.html', context={'history':history})

def sick_regs(request):
    if request.user.is_authenticated:
        regs = SickRegistry.objects.all().order_by('-id')
        return render(request, 'reg_jounals/sick_regs.html', context={'regs':regs})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def create_SickRegistry(request, sr_number):
    if request.user.is_authenticated:
        positions = SickDocument.objects.filter(sd_reg_number__exact=sr_number)
        print(positions)
        count = len(positions)
        return render(request, 'reg_jounals/sick_reg_create.html', context={'positions':positions, 'rnum':sr_number, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def add_SickRegistry(request):
    if request.user.is_authenticated:
        reg_form = SickRegistry_form()
        regs = SickRegistry.objects.all().order_by('sr_number')
        user_ = request.user.first_name
        reg_form.saveFirst(user_)

    else:
        return render(request, 'reg_jounals/no_auth.html')
    return redirect('/journals/sick_regs')

def add_SickDocument(request, sr_number_):
    if request.user.is_authenticated:
        doc_form = SickDocument_form()
        if request.method == "POST":
            doc_form = SickDocument_form(request.POST)
            if doc_form.is_valid():
                user_ = request.user.first_name
                doc_form.saveFirst(user_, sr_number_)
                loc = '/journals/sick_reg/'+str(sr_number_)+'/create/'
                return redirect(loc)
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/SickDocument_add.html', context={'form':doc_form, 'reg_num':sr_number_})

def ItemDel_SickList(request, id):
    if request.user.is_authenticated:
        item = SickDocument.objects.get(id__iexact=id)
        num = item.sd_reg_number
        dest = '/journals/sick_reg/' + str(num) + '/create/'
        item.delete()
        return redirect(dest)
