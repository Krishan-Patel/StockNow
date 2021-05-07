from django.contrib import admin

# Register your models here.
from .models import Stock

#class StockAdmin(admin.ModelAdmin):
 #   list_display = ('identifier', 'day_high', 'low', 'current', 'change', 'pchange', '365', 'lastupdate')
  #  fields = ['identifier', 'day_high', 'day_low', 'current', 'change', 'pchange', 'pchange365', 'last_update']

admin.site.register(Stock)