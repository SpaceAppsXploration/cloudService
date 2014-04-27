from django.contrib import admin
from models import Targets, Missions, Details, Planets
from django.db.models import Q

class TargetsAdmin(admin.ModelAdmin):
    pass
        
class MissionsAdmin(admin.ModelAdmin):
    pass

class DetailsAdmin(admin.ModelAdmin):
    pass
        
    
admin.site.register(Targets, TargetsAdmin)
admin.site.register(Missions, MissionsAdmin)
admin.site.register(Details, DetailsAdmin)
