from django.contrib import admin
from .models import Card

# Register your models here.

class CardAdmin(admin.ModelAdmin):
    list_display = ("card_title", "card_desc", "card_image")


admin.site.register(Card, CardAdmin)