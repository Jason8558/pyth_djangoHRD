from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator

page_count = 15

def index(request):
    if request.user.is_authenticated:
        return render(request, 'reg_jounals/index.html')
    else: return redirect('/accounts/login/')
def outbound_docs(request):
    if request.user.is_authenticated:
        auth = request.user.is_authenticated
        documents = OutBoundDocument.objects.all()
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
    if request.method == "POST":
        doc_form = OutBoundDocument_form(request.POST)
        if doc_form.is_valid():
            user_ = request.user.first_name

            doc_form.doc_res_officer = user_
            print(str(doc_form.doc_res_officer))
            doc_form.saveFirst(user_)
            return redirect('../outbound_docs/')
    else:
        doc_form = OutBoundDocument_form()
    return render(request, 'reg_jounals/outboundDocs_add.html', {'form':doc_form})

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
        letters = LetterOfResignation.objects.all()
        count = len(letters)
        p_letters = Paginator(letters, page_count)
        page_number = request.GET.get('page', 1)
        page = p_letters.get_page(page_number)

        return render(request, 'reg_jounals/letters_of_resignation.html', context={'letters':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')


def nr_LetterOfResignation(request):
    if request.user.is_authenticated:
        letter_form = LetterOfResignation_form()
        if request.method == "POST":
            letter_form = LetterOfResignation_form(request.POST)
            if letter_form.is_valid():
                user_ = request.user.first_name
                letter_form.saveFirst(user_)
                return redirect('../letters_of_resignation/')


    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/LetterOfResignation_add.html', context={'form':letter_form})

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
            letters = LetterOfInvite.objects.all()
            count = len(letters)
            p_letters = Paginator(letters, page_count)
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
        if request.method == 'POST':
            letter_form = LetterOfInvite_form(request.POST)
            if letter_form.is_valid():
                user_ = request.user.first_name
                letter_form.saveFirst(user_)
                return redirect('../letters_of_invite/')
        return render(request, 'reg_jounals/LetterOfInvite_add.html', context={'form':letter_form})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def del_LetterOfInvite(request, id):
    if request.user.is_authenticated:
        letter = LetterOfInvite.objects.get(id__iexact=id)
        letter.delete()
        return redirect('/journals/letters_of_invite')

def order_other_matters(request):
    if request.user.is_authenticated:
        orders = OrdersOnOtherMatters.objects.all()
        p_orders = Paginator(orders, page_count)
        page_number = request.GET.get('page', 1)
        page = p_orders.get_page(page_number)
        count = len(orders)
        return render(request, 'reg_jounals/orders_on_others.html', context={'orders':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def nr_OrderOnOtherMatters(request):
    if request.user.is_authenticated:
        order_form = OrdersOnOtherMatters_form()
        if request.method == "POST":
            order_form =OrdersOnOtherMatters_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../orders_on_others/')


            else:
                return render(request, 'reg_jounals/no_auth.html')
        return render(request, 'reg_jounals/OrdersOnOtherMatters_add.html', context={'form':order_form})

def upd_OrderOnOtherMatters(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            order = OrdersOnOtherMatters.objects.get(id__iexact=id)
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
        orders =OrdersOnVacation.objects.all()
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
        if request.method == "POST":
            order_form =OrdersOnVacation_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../orders_on_vacation/')


            else:
                return render(request, 'reg_jounals/no_auth.html')
        return render(request, 'reg_jounals/OrdersOnVacation_add.html', context={'form':order_form, 'depts':depts})

def upd_OrderOnVacation(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            order = OrdersOnVacation.objects.get(id__iexact=id)
            bound_form = OrdersOnVacation_form(instance=order)
            return render(request, 'reg_jounals/OrdersOnVacation_upd.html', context={'form':bound_form, 'order':order})
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
        orders = OrdersOfBTrip.objects.all()
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
        if request.method == "POST":
            order_form =OrdersOfBTrip_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../orders_of_BTrip/')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/OrdersOfBTrip_add.html', context={'form':order_form, 'depts':depts})

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
        orders = OrdersOnPersonnel.objects.all()
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
        if request.method == "POST":
            order_form =OrdersOnPersonnel_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../orders_on_personnel/')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/OrdersOnPersonnel_add.html', context={'form':order_form, 'depts':depts})


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
        contracts = LaborContract.objects.all()
        p_orders = Paginator(contracts, page_count)
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
        if request.method == "POST":
            order_form = LaborContract_form(request.POST)
            if order_form.is_valid():
                user_ = request.user.first_name
                order_form.saveFirst(user_)
                return redirect('../laborContracts/')
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'reg_jounals/laborContract_add.html', context={'form':order_form, 'depts':depts})

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
            histories = EmploymentHistory.objects.filter(eh_number__exact=search_query)
            print(histories)
        else:
            histories = EmploymentHistory.objects.all()
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
