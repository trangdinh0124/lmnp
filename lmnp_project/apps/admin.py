from django.contrib import admin

from lmnp_project.apps.models import Facture, Receipt

class FactureAdmin(admin.ModelAdmin):
    list_display = ("facture_type", "amount_ttc", "date_facturation")
    search_fields = ("facture_type", "amount_ttc", "date_facturation")
admin.site.register(Facture, FactureAdmin)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("receipt_type", "amount_ttc", "date_receipt")
    search_fields = ("receipt_type", "amount_ttc", "date_receipt")
admin.site.register(Receipt, ReceiptAdmin)