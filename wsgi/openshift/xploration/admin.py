from django.contrib import admin
from models import Targets, Missions, Details, Planets, PayloadBusTypes, PayloadBusComps
from django.db.models import Q
from django import forms

class TargetsAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(TargetsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'characteristics' or db_field.name == 'curiosities' or db_field.name == 'sim_related':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
        
class MissionsAdmin(admin.ModelAdmin):
    pass

class DetailsAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(DetailsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'body':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

class PlanetsAdmin(admin.ModelAdmin):
    pass    

class PayloadBusTypesAdmin(admin.ModelAdmin):
    pass

class PayloadBusCompsAdmin(admin.ModelAdmin):
    pass
 
admin.site.register(Targets, TargetsAdmin)
admin.site.register(Missions, MissionsAdmin)
admin.site.register(Details, DetailsAdmin)
admin.site.register(Planets, PlanetsAdmin)
admin.site.register(PayloadBusComps, PayloadBusCompsAdmin)
admin.site.register(PayloadBusTypes, PayloadBusTypesAdmin)


