from django.contrib import admin

# Register your models here.
from .models import Banknote

class BanknoteAdmin(admin.ModelAdmin):
    list_display = ("country", "denomination", "currency", "pick", "year", "grade", "composition")

admin.site.register(Banknote, BanknoteAdmin)
