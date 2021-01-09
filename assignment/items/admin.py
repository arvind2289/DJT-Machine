#from django.contrib import admin

from django.contrib import admin
from .models import Items,CategoryA



@admin.register(Items)
class AdminItems(admin.ModelAdmin):
    list_display = ['id',]


@admin.register(CategoryA)
class AdminCategoryA(admin.ModelAdmin):
    list_display = ['id',]
