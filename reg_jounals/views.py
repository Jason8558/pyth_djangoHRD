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

def get_user_name(request):
    username = request.user.first_name
    return JsonResponse(username, safe=False)

def index(request):

    if request.user.is_authenticated:

        user_ = request.user
        u_group = user_.groups.all()
        for group in u_group:
            if (group.name == 'Табельщик') or (group.name == 'Сотрудник РО') :
                return redirect('/turv/')
        user_io = request.user.first_name.split(' ')
        if len(user_io) < 3:
            user_io = str(user_io[0])
        else:
            user_io = str(user_io[1]) + " " +str(user_io[2])
        return render(request, 'reg_jounals/index.html', context={'user_io':user_io})
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
        if date_from and date_to:
            documents = OutBoundDocument.objects.filter(doc_date__range=(date_from, date_to)).order_by('doc_date')
            p_documents = Paginator(documents, 1000)
            page_number = request.GET.get('page', 1)

        else:
            documents = OutBoundDocument.objects.all().order_by('-id')
            p_documents = Paginator(documents, 20)
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
                return redirect('/outbound_docs/')

def del_OutBoundDocument(request, id):
    if request.user.is_authenticated:
        document = OutBoundDocument.objects.get(id__iexact=id)
        document.delete()
        return redirect('/outbound_docs/')

# Заявления на увольнения -----------------------
def letter_of_resignation(request):
    if request.user.is_authenticated:
        search_query = request.GET.get('lor_search','')
        if search_query:
            letters = LetterOfResignation.objects.filter(lor_employee__icontains=search_query)
            p_letters = Paginator(letters, 1000)
            page_number = request.GET.get('page', 1)

        else:
            letters = LetterOfResignation.objects.all().order_by('-id')
            p_letters = Paginator(letters, 20)
            page_number = request.GET.get('page', 1)
        page = p_letters.get_page(page_number)
        count = len(letters)

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
                return redirect('/letters_of_resignation')

def del_LetterOfResignation(request, id):
    if request.user.is_authenticated:
        letter = LetterOfResignation.objects.get(id__iexact=id)
        letter.delete()
        return redirect('/letters_of_resignation')

# Заявления на прием ------------------------------
def letter_of_invite(request):
        if request.user.is_authenticated:
            search_query = request.GET.get('loi_search','')
            if search_query:
                letters = LetterOfInvite.objects.filter(loi_employee__icontains=search_query)
                p_letters = Paginator(letters, 1000)
                page_number = request.GET.get('page', 1)

            else:
                letters = LetterOfInvite.objects.all().order_by('-id')
                p_letters = Paginator(letters, 20)
                page_number = request.GET.get('page', 1)
            page = p_letters.get_page(page_number)
            count = len(letters)


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
                return redirect('/letters_of_invite')

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
        return redirect('/letters_of_invite')

# Приказы по другим вопросам -----------------------
def order_other_matters(request):
    if request.user.is_authenticated:
        group = Group.objects.get(name__icontains='Сотрудник СУП')
        users = group.user_set.all()
        for user in users:
            print(user.first_name)

        res_users = User.objects.all()
        date_from = request.GET.get('oom_search_from','')
        date_to = request.GET.get('oom_search_to', '')
        res_seacrh = request.GET.get('oom_search_res','')
        if date_from and date_to and res_seacrh:
            orders = OrdersOnOtherMatters.objects.filter(oom_date__range=(date_from, date_to)).filter(oom_res_officer__icontains=res_seacrh).order_by('oom_date')
            p_orders = Paginator(orders, 1000)
            page_number = request.GET.get('page', 1)

        else:
            if res_seacrh:
                orders = OrdersOnOtherMatters.objects.filter(oom_res_officer__icontains=res_seacrh).order_by('-id')
                p_orders = Paginator(orders, 1000)
                page_number = request.GET.get('page', 1)
            else:
                if date_from and date_to:
                    orders = OrdersOnOtherMatters.objects.filter(oom_date__range=(date_from, date_to)).order_by('oom_date')
                    p_orders = Paginator(orders, 1000)
                    page_number = request.GET.get('page', 1)
                else:
                    orders = OrdersOnOtherMatters.objects.all().order_by('-id')
                    p_orders = Paginator(orders, 20)
                    page_number = request.GET.get('page', 1)
        page = p_orders.get_page(page_number)

        count = len(orders)
        return render(request, 'reg_jounals/orders_on_others.html', context={'orders':page, 'count':count, 'res_users':users})
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
        deps = Departments.objects.all()
        search_query = request.GET.get('bt_search','')
        search_query_dep = request.GET.get('bt_search_dep','')
        if search_query:
            orders = OrdersOfBTrip.objects.filter(bt_emloyer__icontains=search_query)
            p_orders = Paginator(orders, 1000)
            page_number = request.GET.get('page', 1)
        else:
            if search_query_dep:
                orders = OrdersOfBTrip.objects.filter(bt_dep_id=search_query_dep)
                p_orders = Paginator(orders, 1000)
                page_number = request.GET.get('page', 1)
            else:
                orders = OrdersOfBTrip.objects.all().order_by('-id')
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

def get_ordersBtrip(request):
    if request.user.is_authenticated:
        orders = OrdersOfBTrip.objects.values('id', 'bt_date', 'bt_place', 'bt_number', 'bt_emloyer', 'bt_res_officer', 'bt_dep__dep_name')
        orders = list(orders)
        return JsonResponse(orders, safe=False)

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
        search_query = request.GET.get('op_search','')
        date_from = request.GET.get('op_search_from','')
        date_to = request.GET.get('op_search_to', '')
        if date_from and date_to:
            orders = OrdersOnPersonnel.objects.filter(op_date__range=(date_from, date_to)).order_by('op_date')
            p_orders = Paginator(orders, 1000)
            page_number = request.GET.get('page', 1)
        else:
            if search_query:
                orders = OrdersOnPersonnel.objects.filter(op_emloyer__icontains=search_query).order_by('-id')
                p_orders = Paginator(orders, 1000)
                page_number = request.GET.get('page', 1)

            else:
                orders = OrdersOnPersonnel.objects.all().order_by('-id')
                p_orders = Paginator(orders, 20)
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
                return redirect('/orders_on_personnel')

def del_OrderOnPersonnel(request, id):
    if request.user.is_authenticated:
        order = OrdersOnPersonnel.objects.get(id__iexact=id)
        order.delete()
        return redirect('/orders_on_personnel')

# Трудовые договоры ---------------------------
def LaborContracts(request):
    if request.user.is_authenticated:
        search_query = request.GET.get('lc_search','')
        if search_query:
            contracts = LaborContract.objects.filter(lc_dep_id=search_query).order_by('-id')
            p_orders = Paginator(contracts, 1000)
            page_number = request.GET.get('page', 1)
        else:
            contracts = LaborContract.objects.all().order_by('-id')
            p_orders = Paginator(contracts, 20)
            page_number = request.GET.get('page', 1)
        deps = Departments.objects.all()
        page = p_orders.get_page(page_number)
        count = len(contracts)
        return render(request, 'reg_jounals/laborContracts.html', context={'orders':page, 'count':count, 'deps':deps})
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
                return redirect('/laborContracts')

def del_LaborContract(request, id):
    if request.user.is_authenticated:
        order = LaborContract.objects.get(id__iexact=id)
        order.delete()
        return redirect('/laborContracts')

# Трудовые книжки -------------------------------
def employment_history(request):
    if request.user.is_authenticated:

        search_query = request.GET.get('eh_search','')
        if search_query:
            histories = EmploymentHistory.objects.filter(eh_employer__icontains=search_query)
            p_orders = Paginator(histories, 10)
            page_number = request.GET.get('page', 1)
        else:
            histories = EmploymentHistory.objects.all().order_by('-id')
            p_orders = Paginator(histories, 10)
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
        deps = Departments.objects.all()
        search_query = request.GET.get('vac_search','')
        sq_dep = request.GET.get('vac_dep_search','')
        if search_query:

            items = NewOrdersOnVacation_item.objects.filter(fio__icontains=search_query)
            items_count = len(items)
            return render(request, 'reg_jounals/vac_search.html', context={'orders':orders, 'items':items, 'search_query':search_query, 'items_count':items_count})
        else:
            if sq_dep:
                dep = Departments.objects.get(id=sq_dep)
                items = NewOrdersOnVacation_item.objects.filter(dep=sq_dep).order_by('-bound_order__order_date')

                items_count = len(items)
                return render(request, 'reg_jounals/vac_search.html', context={'orders':orders, 'items':items, 'search_query':dep.dep_name, 'items_count':items_count})
            else:
                orders = NewOrdersOnVacation.objects.all().order_by('-id')
                count = len(orders)
                p_orders = Paginator(orders, 30)
                page_number = request.GET.get('page', 1)
                page = p_orders.get_page(page_number)
                return render(request, 'reg_jounals/orders_on_vacation_new.html', context={'orders':page, 'count':count, 'deps':deps})
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
        items = NewOrdersOnVacation_item.objects.filter(bound_order__exact=id)
        order = NewOrdersOnVacation.objects.get(id=id)
        items_count = len(items)
        return render(request, 'reg_jounals/OrderOnVacation_new_create.html', context={'items':items, 'order':order, 'count':items_count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def new_order_on_vacation_addItem(request, order_id):
    if request.user.is_authenticated:
        item_form = NewOrdersOnVacationItem_form()
        if request.method == "POST":
            item_form = NewOrdersOnVacationItem_form(request.POST)
            if item_form.is_valid():
                user_ = request.user.first_name
                print(order_id)
                item_form.saveFirst(order_id, user_)
                loc = '/orders_on_vacation_new/'+str(order_id)+'/create'
                return redirect(loc)
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/NewOrderOnVacation_addItem.html', context={'form':item_form, 'order_id':order_id})

def new_order_on_vacation_updItem(request, id):
    if request.user.is_authenticated:
        item = NewOrdersOnVacation_item.objects.get(id__exact=id)
        # order = NewOrdersOnVacation.objects.get(id__exact=item.bound_order)
        # b_order = item.bound_order
        if request.method == "GET":
            bound_form = NewOrdersOnVacationItem_form(instance=item)
            return render(request, 'reg_jounals/NewOrderOnVacation_updItem.html', context={'form':bound_form, 'item':item, })
        else:
            item = NewOrdersOnVacation_item.objects.get(id__iexact=id)
            bound_form = NewOrdersOnVacationItem_form(request.POST, instance=item)
            if bound_form.is_valid():
                user_ = request.user.first_name
                bound_form.save()
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
        deps = Departments.objects.all()
        search_query = request.GET.get('ident_search','')
        sq_dep = request.GET.get('ident_dep_search','')
        if search_query:
            ident = Identity.objects.all().order_by('-id').filter(employer__icontains=search_query)
            p_ident = Paginator(ident, 200)
            page_number = request.GET.get('page', 1)
            page = p_ident.get_page(page_number)
        else:
            if sq_dep:
                ident = Identity.objects.all().order_by('-id').filter(department_id=sq_dep)
                p_ident = Paginator(ident, 200)
                page_number = request.GET.get('page', 1)
                page = p_ident.get_page(page_number)
            else:
                ident = Identity.objects.all().order_by('-id')
                p_ident = Paginator(ident, 20)
                page_number = request.GET.get('page', 1)
                page = p_ident.get_page(page_number)
        count = len(ident)
        return render(request, 'reg_jounals/identitys.html', context={'idents':page, 'count':count, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_identitys(request):
    if request.user.is_authenticated:
        ident_form = Identity_form()
        next_num = int(Identity.objects.latest('id').number) + 1
        if request.method == "POST":
            ident_form = Identity_form(request.POST)
            if ident_form.is_valid():
                user_ = request.user.first_name
                ident_form.saveFirst(user_)
                return redirect('/identity')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/identity_add.html', context={'form':ident_form, 'next_num':next_num})

def upd_identitys(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            ident = Identity.objects.get(id__iexact=id)
            bound_form = Identity_form(instance=ident)
            return render(request, 'reg_jounals/identity_upd.html', context={'form':bound_form, 'ind':ident})
        else:
            ident = Identity.objects.get(id__iexact=id)
            bound_form = Identity_form(request.POST, instance=ident)
            if bound_form.is_valid():
                user_ = request.user.first_name
                new_obj = bound_form.save()
                return redirect('/identity')

def del_identitys(request, id):
    if request.user.is_authenticated:
        ident = Identity.objects.get(id__exact=id)


        dest = '/identity'
        ident.delete()
        return redirect(dest)
