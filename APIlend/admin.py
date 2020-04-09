from django.contrib import admin
from .models import UserProfile, DebtMonetary, DebtItem

admin.site.register(UserProfile)
admin.site.register(DebtMonetary)
admin.site.register(DebtItem)

# Register your models here.
