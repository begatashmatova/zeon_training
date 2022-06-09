from django.contrib import admin
from .models import Benefit

# Register your models here.
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')

admin.site.register(Benefit, BenefitAdmin)