from django.contrib import admin
from django.db import models
from models import Targets, Missions, Details, Planets, PayloadBusTypes, PayloadBusComps, SciData

#from django.db.models import Q
from django import forms
from django.forms import SelectMultiple

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
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        '''
        Show only unique values from Missions, eg.(mission,target) coupling
        '''
        if db_field.name == "mission":
            
            d = {}
            for a in Missions.objects.all():
                if not d.get(a.codename):
                    d[a.codename] = a.id  
            
            Alldistinct = set(d.values())
            Alldistinct = Missions.objects.filter(id__in=Alldistinct)
            kwargs["queryset"] = Alldistinct
        return super(DetailsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class PlanetsAdmin(admin.ModelAdmin):
    pass    

class PayloadBusTypesAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PayloadBusTypesAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

class PayloadBusCompsAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PayloadBusCompsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

class SciDataAdmin(admin.ModelAdmin):
    formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'12'})}, }
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(SciDataAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'body':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        if db_field.name == 'comment':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

admin.site.register(Targets, TargetsAdmin)
admin.site.register(Missions, MissionsAdmin)
admin.site.register(Details, DetailsAdmin)
admin.site.register(Planets, PlanetsAdmin)
admin.site.register(PayloadBusComps, PayloadBusCompsAdmin)
admin.site.register(PayloadBusTypes, PayloadBusTypesAdmin)
admin.site.register(SciData, SciDataAdmin)


