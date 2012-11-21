# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.translation import  ugettext_lazy as _

from estates.models import *
from estates.choices import *
from world.models import *

class SomeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SomeForm, self).__init__(*args, **kwargs)
        if self.instance is None and len(self.data) == 0:
            # On create
            self.fields['region'].queryset = Region.objects.filter(country=0)
            self.fields['city'].queryset = City.objects.filter(region=0)
        if self.instance.id and len(self.data) == 0:
            # On edit
            self.fields['region'].queryset = Region.objects.filter(country=self.instance.country)
            self.fields['city'].queryset = City.objects.filter(region=self.instance.region)
            c_name = City.objects.get(pk=self.instance.city.pk)
            self.fields['city_loader'].initial = c_name.name
        if len(self.data) > 0:
            # On POST request
            self.fields['region'].queryset = Region.objects.filter(country=self.data.get('country') or 0)
            self.fields['city'].queryset = City.objects.filter(region=self.data.get('region') or 0)
            # Create new city if not exists
            try:
                self.city = City.objects.get(
                    country=self.data.get('country'),
                    region=self.data.get('region'),
                    name=self.data.get('city_loader'),
                    )
            except :
                self.city = City(
                    country=Country.objects.get(pk=self.data.get('country')),
                    region=Region.objects.get(pk=self.data.get('region')),
                    name=self.data.get('city_loader'),
                )
                self.city.save()

    name_ru = forms.CharField(label=_(u"Название [ru]"))
    name_en = forms.CharField(label=_(u"Название [en]"))
    name_de = forms.CharField(label=_(u"Название [de]"))
    kitchen_type = forms.MultipleChoiceField(choices=KITCHEN_OPTIONS, widget=forms.CheckboxSelectMultiple(),label=_(u'Кухня'), required=False)
    comfort = forms.MultipleChoiceField(choices=COMFORT_OPTIONS, widget=forms.CheckboxSelectMultiple(),label=_(u'Комфорт'), required=False)
    rent_for = forms.MultipleChoiceField(choices=RENT_FOR_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=RentForChoices._meta.verbose_name)
    location = forms.MultipleChoiceField(choices=LOCATION_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=LocationChoices._meta.verbose_name)
    floor_type = forms.MultipleChoiceField(choices=FLOOR_TYPE_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=FloorTypeChoices._meta.verbose_name)
    heating = forms.MultipleChoiceField(choices=HEATING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=HeatingOptions._meta.verbose_name)
    floor_covering = forms.MultipleChoiceField(choices=FLOOR_COVERING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=FloorCoveringOptions._meta.verbose_name)
    kitchen_type = forms.MultipleChoiceField(choices=KITCHEN_OPTIONS, widget=forms.CheckboxSelectMultiple(), required=False, label=KitchenChoices._meta.verbose_name)
    bathroom = forms.MultipleChoiceField(choices=BATHROOM_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=BathroomChoices._meta.verbose_name)
    other_facilies = forms.MultipleChoiceField(choices=OTHER_FACILITIES_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=OtherFacilitieChoices._meta.verbose_name)
    security_systems = forms.MultipleChoiceField(choices=SECURITY_SYSTEMS_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=SecuritySystemsChoices._meta.verbose_name)
    comfort = forms.MultipleChoiceField(choices=COMFORT_OPTIONS, widget=forms.CheckboxSelectMultiple(), required=False, label=ComfortChoices._meta.verbose_name)
    furnishings = forms.MultipleChoiceField(choices=FURNISHING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=FurnishingChoices._meta.verbose_name)
    additional_equipment = forms.MultipleChoiceField(choices=ADDITIONAL_EQUIPMENT_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=AdditionalEquipmentChoices._meta.verbose_name)
    glazing = forms.MultipleChoiceField(choices=GLAZING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=GlazingChoices._meta.verbose_name)
    glass_frame = forms.MultipleChoiceField(choices=GLASS_FRAME_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=GlassFrameChoices._meta.verbose_name)
    window_view = forms.MultipleChoiceField(choices=WINDOW_VIEW_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=WindowViewChoices._meta.verbose_name)
    condition = forms.MultipleChoiceField(choices=CONDITION_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=ConditionChoices._meta.verbose_name)
    region = forms.ModelChoiceField(queryset=Region.objects.filter(id=0))
    city = forms.ModelChoiceField(queryset=Region.objects.filter(id=0), widget=forms.TextInput())
    city_loader = forms.CharField()

    def save(self, *args, **kwargs):
        self.instance.city = self.city
        return super(SomeForm, self).save(commit=False)

    class  Meta:
        model = Apartament
        exclude = ['name','description', 'object_location']

    class Media:
        js = ('/media/jquery/js/jquery-1.4.4.min.js',
              '/media/jquery/js/jquery-ui-1.8.9.custom.min.js',
              '/media/scripts/jquery.relatedselects.min.js',
              '/media/adminScripts/estatesForm.js',
        )

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

# Make objects published
def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)
make_published.short_description = _(u"Опубликовать")

# Make objects unpublished
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)
make_unpublished.short_description = _(u"Снять публикацию")

class AdminApartament(admin.ModelAdmin):
    list_filter = ['type', 'is_published']
    list_display = ['name','price','type','country','city','is_published','created']
    search_fields = ['id', 'name', 'country__name', 'user__email']
    inlines = [PhotoInline]
    actions = [make_published, make_unpublished]
    form = SomeForm

class AdminEstateTypeSeoTextForm(forms.ModelForm):
    class Meta:
        exclude = ['description']

class AdminEstateTypeSeoText(admin.ModelAdmin):
    form = AdminEstateTypeSeoTextForm
    class Media:
        js = ['/admin_media/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/admin_media/tinymce_setup/tinymce_setup.js',]
                

admin.site.register(Apartament, AdminApartament)
admin.site.register(EstateTypeSeoText, AdminEstateTypeSeoText)
