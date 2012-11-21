# -*- coding: utf-8 -*-
from django.contrib import admin

from tarifs.models import Tarif, TarifRequests

class AdminTarif(admin.ModelAdmin):
    list_display = ['name','price', 'price_per_ad', 'ad_count']

class AdminTarifRequests(admin.ModelAdmin):
    list_display = ['user', 'tarif', 'months_count', 'paid', 'start_date', 'end_date']
    search_fields = ['user__email']
    list_filter = ['tarif', 'paid']

admin.site.register(Tarif, AdminTarif)
admin.site.register(TarifRequests, AdminTarifRequests)
