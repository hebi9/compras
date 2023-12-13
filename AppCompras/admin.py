from django.contrib import admin
from .models import Listas, DetalleLista

# Register your models here.
class listAdmin(admin.ModelAdmin):
    list_filter = ['lista']

admin.site.register(Listas)
admin.site.register(DetalleLista,listAdmin)