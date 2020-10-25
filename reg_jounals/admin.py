from django.contrib import admin
from .models import *




class OutBoundDocumentAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.doc_res_officer = request.user.first_name
        obj.save()

admin.site.register(OutBoundDocument, OutBoundDocumentAdmin)
admin.site.register(LetterOfResignation)
admin.site.register(LetterOfInvite)
admin.site.register(OrdersOnOtherMatters)
