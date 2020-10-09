from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, 'reg_jounals/index.html')
def outbound_docs(request):
    documents = OutBoundDocument.objects.all()
    count = len(documents)
    return render(request, 'reg_jounals/outbound_docs.html', context={'documents':documents, 'count':count})
