from django.contrib import admin
from .models import *

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'title',
        'writer',
        'team',
        'github',
        'introduction',
        'created_at',
    )