from django.contrib import admin
from .models import *




class OutBoundDocumentAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.doc_res_officer = request.user.first_name
        obj.save()

admin.site.register(OutBoundDocument, OutBoundDocumentAdmin)
admin.site.register(EmploymentHistory)
admin.site.register(LaborContract)
admin.site.register(LetterOfInvite)
admin.site.register(LetterOfResignation)
admin.site.register(OrdersOfBTrip)
admin.site.register(OrdersOnPersonnel)
admin.site.register(OrdersOnVacation)
admin.site.register(OrdersOnOtherMatters)
admin.site.register(Departments)
admin.site.register(SickRegistry)
admin.site.register(SickDocument)
admin.site.register(NewOrdersOnVacation)
admin.site.register(NewOrdersOnVacation_item)
admin.site.register(Identity)
