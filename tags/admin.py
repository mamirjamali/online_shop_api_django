from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # define tag class for admin site
    search_fields = ['lable']
