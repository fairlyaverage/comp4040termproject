from django.contrib import admin
from .models import Moment # , Momenteer

# admin site displays for models
@admin.register(Moment) # decorator reg
class MomentAdmin(admin.ModelAdmin):
    pass

# @admin.register(Momenteer)
# class MomenteerAdmin(admin.ModelAdmin):
#     pass
