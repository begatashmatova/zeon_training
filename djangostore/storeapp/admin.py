from django.contrib import admin
from .models import Benefit
from .models import Collection

# Register your models here.
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')

admin.site.register(Benefit, BenefitAdmin)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')

admin.site.register(Collection, CollectionAdmin)