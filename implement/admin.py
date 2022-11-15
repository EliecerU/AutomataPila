from django.contrib import admin

# Register your models here.

from .models import Validate

class AdminValidate(admin.ModelAdmin):
    list_display = ['word']
    class Meta:
        model = Validate

admin.site.register(Validate, AdminValidate)

