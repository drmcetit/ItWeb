from django.contrib import admin

from .models import carouselModel,AssosiationMembersModel,PlacementModel

# Register your models here.

admin.site.register(carouselModel)

class AssosiationAdmin(admin.ModelAdmin):
    list_filter=('Year',)
admin.site.register(AssosiationMembersModel)

class PlacementAdmin(admin.ModelAdmin):
    list_filter=('Batch','Placed','StartUp')
    list_display=('Name','Batch','Company','LPA')
admin.site.register(PlacementModel)
