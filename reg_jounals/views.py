from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, 'reg_jounals/index.html')
def outbound_docs(request):
    if request.user.is_authenticated:
        documents = OutBoundDocument.objects.all()
        count = len(documents)
        method = str(request.method)
        usr = str(request.user.first_name)
        return render(request, 'reg_jounals/outbound_docs.html', context={'documents':documents, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')
