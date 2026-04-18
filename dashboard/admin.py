from django.contrib import admin
from .models import CrimeRecord


@admin.register(CrimeRecord)
class CrimeRecordAdmin(admin.ModelAdmin):
    list_display = ('province_or_territory', 'year', 'metric', 'value')
    search_fields = ('province_or_territory', 'metric')
    list_filter = ('province_or_territory', 'year')