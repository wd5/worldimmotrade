# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import  ugettext_lazy as _
from django.utils import translation
from django.utils.text import get_text_list, capfirst

from estates.models import *
from estates.choices import *
from world.models import *

class ApartmentForm(forms.ModelForm):
    ''' Form for create edit apartments '''
    def __init__(self, *args, **kwargs):
        super(ApartmentForm, self).__init__(*args, **kwargs)
        self.fields['country'].label = _(u'Страна')
        if self.instance is None and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=0)
            self.fields['city'].queryset = City.objects.filter(region=0)
        if self.instance.id and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.instance.country)
            self.fields['city'].queryset = City.objects.filter(region=self.instance.region)
        if len(self.data) > 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.data.get('country') or 0)
            self.fields['city'].queryset = City.objects.filter(region=self.data.get('region') or 0)

    if translation.get_language() == 'ru':
        country_set = Country.objects.order_by('name_ru').all()
    if translation.get_language() == 'en':
        country_set = Country.objects.order_by('name_en').all()
    if translation.get_language() == 'de':
        country_set = Country.objects.order_by('name_de').all()

    country = forms.ModelChoiceField(queryset=country_set, label=_(u"Страна"), empty_label=_(u"--Страна--"))

    name_ru = forms.CharField(label=_(u"Название [ru]"))
    name_en = forms.CharField(label=_(u"Название [en]"))
    name_de = forms.CharField(label=_(u"Название [de]"))
    kitchen_type = forms.MultipleChoiceField(choices=KITCHEN_OPTIONS, widget=forms.CheckboxSelectMultiple(),label=capfirst(_(u'Кухня')), required=False)
    comfort = forms.MultipleChoiceField(choices=COMFORT_OPTIONS, widget=forms.CheckboxSelectMultiple(),label=capfirst(_(u'Комфорт')), required=False)
    rent_for = forms.MultipleChoiceField(choices=RENT_FOR_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(RentForChoices._meta.verbose_name))
    location = forms.MultipleChoiceField(choices=LOCATION_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(LocationChoices._meta.verbose_name))
    floor_type = forms.MultipleChoiceField(choices=FLOOR_TYPE_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(FloorTypeChoices._meta.verbose_name))
    heating = forms.MultipleChoiceField(choices=HEATING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(HeatingOptions._meta.verbose_name))
    floor_covering = forms.MultipleChoiceField(choices=FLOOR_COVERING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(FloorCoveringOptions._meta.verbose_name))
    kitchen_type = forms.MultipleChoiceField(choices=KITCHEN_OPTIONS, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(KitchenChoices._meta.verbose_name))
    bathroom = forms.MultipleChoiceField(choices=BATHROOM_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(BathroomChoices._meta.verbose_name))
    other_facilies = forms.MultipleChoiceField(choices=OTHER_FACILITIES_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(OtherFacilitieChoices._meta.verbose_name))
    security_systems = forms.MultipleChoiceField(choices=SECURITY_SYSTEMS_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(SecuritySystemsChoices._meta.verbose_name))
    comfort = forms.MultipleChoiceField(choices=COMFORT_OPTIONS, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(ComfortChoices._meta.verbose_name))
    furnishings = forms.MultipleChoiceField(choices=FURNISHING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(FurnishingChoices._meta.verbose_name))
    additional_equipment = forms.MultipleChoiceField(choices=ADDITIONAL_EQUIPMENT_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(AdditionalEquipmentChoices._meta.verbose_name))
    glazing = forms.MultipleChoiceField(choices=GLAZING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(GlazingChoices._meta.verbose_name))
    glass_frame = forms.MultipleChoiceField(choices=GLASS_FRAME_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(GlassFrameChoices._meta.verbose_name))
    window_view = forms.MultipleChoiceField(choices=WINDOW_VIEW_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(WindowViewChoices._meta.verbose_name))
    condition =forms.MultipleChoiceField(choices=CONDITION_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(ConditionChoices._meta.verbose_name))
    region = forms.ModelChoiceField(queryset=Region.objects.filter(id=0), label=capfirst(_(u"Регион")))
    city = forms.ModelChoiceField(queryset=City.objects.filter(id=0), label=capfirst(_(u"Город")))

    required_css_class = 'required'

    class  Meta:
        model = Apartament
        exclude = ['show_on_start_page','students','is_published','user', 'name', 'description', 'object_location', 'views']

class ApartmentViewForm(forms.ModelForm):
    ''' Form for view apartments '''
    def __init__(self, *args, **kwargs):
        super(ApartmentViewForm, self).__init__(*args, **kwargs)
        self.fields['country'].label = _(u'Страна')
        if self.instance is None and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=0)
            self.fields['city'].queryset = City.objects.filter(region=0)
        if self.instance.id and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.instance.country)
            self.fields['city'].queryset = City.objects.filter(region=self.instance.region)
        if len(self.data) > 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.data.get('country') or 0)
            self.fields['city'].queryset = City.objects.filter(region=self.data.get('region') or 0)

    kitchen_type = forms.MultipleChoiceField(choices=KITCHEN_OPTIONS, widget=forms.CheckboxSelectMultiple(),label=capfirst(_(u'Кухня')), required=False)
    comfort = forms.MultipleChoiceField(choices=COMFORT_OPTIONS, widget=forms.CheckboxSelectMultiple(),label=capfirst(_(u'Комфорт')), required=False)
    rent_for = forms.MultipleChoiceField(choices=RENT_FOR_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(RentForChoices._meta.verbose_name))
    location = forms.MultipleChoiceField(choices=LOCATION_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(LocationChoices._meta.verbose_name))
    floor_type = forms.MultipleChoiceField(choices=FLOOR_TYPE_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(FloorTypeChoices._meta.verbose_name))
    heating = forms.MultipleChoiceField(choices=HEATING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(HeatingOptions._meta.verbose_name))
    floor_covering = forms.MultipleChoiceField(choices=FLOOR_COVERING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(FloorCoveringOptions._meta.verbose_name))
    kitchen_type = forms.MultipleChoiceField(choices=KITCHEN_OPTIONS, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(KitchenChoices._meta.verbose_name))
    bathroom = forms.MultipleChoiceField(choices=BATHROOM_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(BathroomChoices._meta.verbose_name))
    other_facilies = forms.MultipleChoiceField(choices=OTHER_FACILITIES_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(OtherFacilitieChoices._meta.verbose_name))
    security_systems = forms.MultipleChoiceField(choices=SECURITY_SYSTEMS_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(SecuritySystemsChoices._meta.verbose_name))
    comfort = forms.MultipleChoiceField(choices=COMFORT_OPTIONS, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(ComfortChoices._meta.verbose_name))
    furnishings = forms.MultipleChoiceField(choices=FURNISHING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(FurnishingChoices._meta.verbose_name))
    additional_equipment = forms.MultipleChoiceField(choices=ADDITIONAL_EQUIPMENT_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(AdditionalEquipmentChoices._meta.verbose_name))
    glazing = forms.MultipleChoiceField(choices=GLAZING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(GlazingChoices._meta.verbose_name))
    glass_frame = forms.MultipleChoiceField(choices=GLASS_FRAME_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(GlassFrameChoices._meta.verbose_name))
    window_view = forms.MultipleChoiceField(choices=WINDOW_VIEW_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(WindowViewChoices._meta.verbose_name))
    condition =forms.MultipleChoiceField(choices=CONDITION_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(ConditionChoices._meta.verbose_name))
    region = forms.ModelChoiceField(queryset=Region.objects.filter(id=0), label=capfirst(_(u"Регион")))
    city = forms.ModelChoiceField(queryset=City.objects.filter(id=0), label=capfirst(_(u"Город")))

    required_css_class = 'required'

    class  Meta:
        model = Apartament
        exclude = ['students','show_on_start_page', 'is_published','user', 'description_en', 'description_de','description_ru','name_ru','name_en','name_de', 'object_location_en','object_location_ru','object_location_de' ]

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['apartament']

class SearchForm(forms.ModelForm):
    ''' Form for process search queries '''
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        if len(self.data) > 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.data.get('country') or -1)
            self.fields['city'].queryset = City.objects.filter(region=self.data.get('region') or -1)

    ESTATE_TYPE_CHOICES2 = list((('0',capfirst(_(u"--Тип Недвижимости--"))),)) + list(ESTATE_TYPE_CHOICES)
    ESTATE_TYPE_CHOICES3 = list((('0',capfirst(_(u"--Тип Недвижимости--"))),)) + list(ESTATE_TYPE_CHOICES_STUDENTS)

    RENT_FOR_CHOICES2 = (
        (1, capfirst(_(u"Мужчина"))),
        (2, capfirst(_(u"Женщина"))),
        (3, capfirst(_(u"Аренда для курящего"))),
        (4, capfirst(_(u"Аренда для некурящего")))
    )

    if translation.get_language() == 'ru':
        country_set = Country.objects.order_by('name_ru').all()
    if translation.get_language() == 'en':
        country_set = Country.objects.order_by('name_en').all()
    if translation.get_language() == 'de':
        country_set = Country.objects.order_by('name_de').all()

    country = forms.ModelChoiceField(queryset=country_set, label=capfirst(_(u"Страна")), empty_label=capfirst(_(u"--Страна--")))
    region = forms.ModelChoiceField(queryset=Region.objects.filter(id=0), label=capfirst(_(u"Регион")), empty_label=capfirst(_(u"--Регион--")))
    city = forms.ModelChoiceField(queryset=City.objects.filter(id=0), label=capfirst(_(u"Город")), empty_label=capfirst(_(u"--Город--")))
    estate_type = forms.ChoiceField(choices=ESTATE_TYPE_CHOICES2, label=capfirst(_(u"--Тип недвижимости--")))
    estate_type_students = forms.ChoiceField(choices=ESTATE_TYPE_CHOICES3, label=capfirst(_(u"--Тип недвижимости--")))
    floor_type = forms.MultipleChoiceField(choices=FLOOR_TYPE_CHOICES, label=capfirst(_(u"Тип этажа")), widget=forms.CheckboxSelectMultiple())
    window_view = forms.MultipleChoiceField(choices=WINDOW_VIEW_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(WindowViewChoices._meta.verbose_name))
    location = forms.MultipleChoiceField(choices=LOCATION_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(LocationChoices._meta.verbose_name))
    furnishings = forms.MultipleChoiceField(choices=FURNISHING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(FurnishingChoices._meta.verbose_name))
    comfort = forms.MultipleChoiceField(choices=COMFORT_OPTIONS, widget=forms.CheckboxSelectMultiple(),label=capfirst(_(u'Комфорт')), required=False)
    price_min = forms.CharField()
    price_max = forms.CharField()
    additional_equipment = forms.MultipleChoiceField(choices=ADDITIONAL_EQUIPMENT_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=AdditionalEquipmentChoices._meta.verbose_name)
    floor_start = forms.CharField()
    floor_end = forms.CharField()
    rooms_start = forms.CharField()
    rooms_end = forms.CharField()
    sleep_rooms_start = forms.CharField()
    sleep_rooms_end = forms.CharField()
    year_start = forms.CharField()
    year_end = forms.CharField()
    aviable_start = forms.CharField()
    aviable_end = forms.CharField()
    total_space_start = forms.CharField()
    total_space_end = forms.CharField()
    rent_for = forms.MultipleChoiceField(choices=RENT_FOR_CHOICES2, widget=forms.CheckboxSelectMultiple(), required=False)

    class Meta:
        model = Apartament
        exclude = ['students','for_students','only_for_students']

class SearchFormMini(forms.ModelForm):
    ''' Form for process search queries '''
    def __init__(self,request, *args, **kwargs):
        super(SearchFormMini, self).__init__( *args, **kwargs)
        if len(self.data) > 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.data.get('country') or -1)
            self.fields['city'].queryset = City.objects.filter(region=self.data.get('region') or -1)

	host = request.get_host()
        if host.endswith('.com'):
            self.fields['country'].queryset = Country.objects.order_by('name_en').all()
        if host.endswith('.de'):
            self.fields['country'].queryset = Country.objects.order_by('name_de').all()
        if host.endswith('.ru'):
            self.fields['country'].queryset = Country.objects.order_by('name_ru').all()


    ESTATE_TYPE_CHOICES2 = list((('0',capfirst(_(u"--Тип Недвижимости--"))),)) + list(ESTATE_TYPE_CHOICES_MINI)
    ESTATE_TYPE_CHOICES3 = list((('0',capfirst(_(u"--Тип Недвижимости--"))),)) + list(ESTATE_TYPE_CHOICES_STUDENTS)

    RENT_FOR_CHOICES2 = (
        (1, capfirst(_(u"Мужчина"))),
        (2, capfirst(_(u"Женщина"))),
        (3, capfirst(_(u"Аренда для курящего"))),
        (4, capfirst(_(u"Аренда для некурящего")))
    )

    country = forms.ModelChoiceField(queryset=Country.objects.all(), label=_(u"Страна"), empty_label=capfirst(_(u"--Страна--")))
    region = forms.ModelChoiceField(queryset=Region.objects.filter(id=0), label=capfirst(_(u"Регион")), empty_label=capfirst(_(u"--Регион--")))
    city = forms.ModelChoiceField(queryset=City.objects.filter(id=0), label=capfirst(_(u"Город")), empty_label=capfirst(_(u"--Город--")))
    estate_type = forms.ChoiceField(choices=ESTATE_TYPE_CHOICES2, label=capfirst(_(u"--Тип недвижимости--")))
    estate_type_students = forms.ChoiceField(choices=ESTATE_TYPE_CHOICES3, label=capfirst(_(u"--Тип недвижимости--")))
    floor_type = forms.MultipleChoiceField(choices=FLOOR_TYPE_CHOICES, label=capfirst(_(u"Тип этажа")), widget=forms.CheckboxSelectMultiple())
    window_view = forms.MultipleChoiceField(choices=WINDOW_VIEW_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(WindowViewChoices._meta.verbose_name))
    location = forms.MultipleChoiceField(choices=LOCATION_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(LocationChoices._meta.verbose_name))
    furnishings = forms.MultipleChoiceField(choices=FURNISHING_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(FurnishingChoices._meta.verbose_name))
    comfort = forms.MultipleChoiceField(choices=COMFORT_OPTIONS, widget=forms.CheckboxSelectMultiple(),label=capfirst(_(u'Комфорт')), required=False)
    price_min = forms.CharField()
    price_max = forms.CharField()
    additional_equipment = forms.MultipleChoiceField(choices=ADDITIONAL_EQUIPMENT_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False, label=capfirst(AdditionalEquipmentChoices._meta.verbose_name))
    floor_start = forms.CharField()
    floor_end = forms.CharField()
    rooms_start = forms.CharField()
    rooms_end = forms.CharField()
    sleep_rooms_start = forms.CharField()
    sleep_rooms_end = forms.CharField()
    year_start = forms.CharField()
    year_end = forms.CharField()
    aviable_start = forms.CharField()
    aviable_end = forms.CharField()
    total_space_start = forms.CharField()
    total_space_end = forms.CharField()
    rent_for = forms.MultipleChoiceField(choices=RENT_FOR_CHOICES2, widget=forms.CheckboxSelectMultiple(), required=False)

    class Meta:
        model = Apartament
        exclude = ['students','for_students','only_for_students']

