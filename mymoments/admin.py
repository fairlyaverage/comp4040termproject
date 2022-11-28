from django.contrib import admin
from .models import Moment

# admin site displays for models
@admin.register(Moment) # decorator reg
class MomentAdmin(admin.ModelAdmin):
    pass
