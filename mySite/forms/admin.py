from django.contrib import admin
from forms.models import Forms

# Register your models here.

class FormsAdmin(admin.ModelAdmin):
    list_display = ("Name", "Email Address", "Password")

admin.site.register(Forms)