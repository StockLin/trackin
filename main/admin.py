from django.contrib import admin
from main.models import Contacts
# Register your models here.

@admin.register(Contacts)
class contactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'send_date')
    ordering = ('-send_date', )
