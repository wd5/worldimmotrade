# -*- coding: utf-8 -*-
import Image
import os

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import  ugettext_lazy as _
from django.conf import settings

from annoing.currencyManager import currencyManager
from estates.choices import *
from world.models import *
        
class  KitchenChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=KITCHEN_OPTIONS)
    use_list = KITCHEN_OPTIONS
    
    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(KITCHEN_OPTIONS[index][1])

    class Meta:
        verbose_name = _(u"Кухня")

class  ComfortChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=COMFORT_OPTIONS)
    use_list = COMFORT_OPTIONS
    
    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(COMFORT_OPTIONS[index][1])

    class Meta:
        verbose_name = _(u"Комфорт")

class  RentForChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=RENT_FOR_CHOICES)
    use_list = RENT_FOR_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(RENT_FOR_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Сдается арендатору")

class  LocationChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=LOCATION_CHOICES)
    use_list = LOCATION_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(LOCATION_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Расположение")

class  FloorTypeChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=FLOOR_TYPE_CHOICES)
    use_list = FLOOR_TYPE_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(FLOOR_TYPE_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Тип этажа")

class  HeatingOptions(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=HEATING_CHOICES)
    use_list = HEATING_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(HEATING_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Тип отопления")

class  FloorCoveringOptions(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=FLOOR_COVERING_CHOICES)
    use_list = FLOOR_COVERING_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(HEATING_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Покрытие пола")

class  BathroomChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=BATHROOM_CHOICES)
    use_list = BATHROOM_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(BATHROOM_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Ванная комната")

class  OtherFacilitieChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=OTHER_FACILITIES_CHOICES)
    use_list = OTHER_FACILITIES_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(OTHER_FACILITIES_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Другие помещения")

class  SecuritySystemsChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=SECURITY_SYSTEMS_CHOICES)
    use_list = SECURITY_SYSTEMS_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(SECURITY_SYSTEMS_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Системы безопасности")

class  FurnishingChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=FURNISHING_CHOICES)
    use_list = FURNISHING_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(FURNISHING_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Меблировка")

class  AdditionalEquipmentChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=ADDITIONAL_EQUIPMENT_CHOICES)
    use_list = ADDITIONAL_EQUIPMENT_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(ADDITIONAL_EQUIPMENT_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Дополнительное оснащение")


class  GlazingChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=GLAZING_CHOICES)
    use_list = GLAZING_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(GLAZING_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Остекление")


class  GlassFrameChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=GLASS_FRAME_CHOICES)
    use_list = GLASS_FRAME_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(GLASS_FRAME_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Стекольные рамы")

class  WindowViewChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=WINDOW_VIEW_CHOICES)
    use_list = WINDOW_VIEW_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(WINDOW_VIEW_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Вид из окна")


class  ConditionChoices(models.Model):
    options = models.CharField(max_length=15, blank = True, choices=CONDITION_CHOICES)
    use_list = CONDITION_CHOICES

    def __unicode__(self):
        index = int(self.options) - 1
        return unicode(CONDITION_CHOICES[index][1])

    class Meta:
        verbose_name = _(u"Состояние")


class Apartament(models.Model):
    '''
    Model for handling all objects and its relations
    '''
    def __init__(self,*args,**kwargs):
        super(Apartament, self).__init__(*args,**kwargs)

    user = models.ForeignKey(User)
    # Determinate is object paid and published
    is_published = models.BooleanField(_(u"Показывать на сайте"), default=0)
    show_on_start_page = models.BooleanField(_(u"Показывать на главной странице"), default=0)
    name = models.CharField(_(u"Название"), max_length=255)
    type = models.CharField(_(u"Тип сделки"), choices=TYPE_CHOICES, blank=False, max_length=5, default=0)
    for_students = models.BooleanField(_(u"Также для студентов"), default=0)
    only_for_students = models.BooleanField(_(u"Только для студентов"), default=0)
    # Determinate show object only in students search
    # See description in save method
    students = models.IntegerField(max_length=1, blank=True, default=0, null=True)
    country = models.ForeignKey(Country, blank=False)
    region = models.ForeignKey(Region, blank=False)
    city = models.ForeignKey(City, blank=False)
    price = models.FloatField(_(u"Цена"), default="")
    client_number = models.CharField(_(u"Номер объекта клиента"), max_length=100, blank=True, null=True)
    #price_for_m2 = models.BooleanField(_(u"м2"), default=0) # Is price for m2?
    commission = models.FloatField(_(u"Комиссионные"), default="", blank=True, null=True)
    additional_costs = models.FloatField(_(u"Дополнительные расходы"), default="", blank=True, null=True)
    prepayment = models.FloatField(_(u"Предоплата/Залог"), default="", blank=True, null=True)
    possible_bargain = models.BooleanField(_(u"Возможен торг"), default=0)
    estate_type = models.CharField(_(u"Тип недвижимости"), max_length=15, choices=ESTATE_TYPE_CHOICES, blank=False)
    # One from next aviable_* options are required
    aviable_from = models.DateField(_(u"Доступна с"), blank=True, null=True)
    aviable_to = models.DateField(_(u"Доступна по"), blank=True, null=True)
    aviable_now = models.BooleanField(_(u"Доступна немедленно"), default=0, blank=True)
    rent_for = models.ManyToManyField(RentForChoices, blank=True, verbose_name=RentForChoices._meta.verbose_name)
    built_year = models.IntegerField(_(u"Год постройки"), max_length=4, blank=True, default="", null=True)
    location = models.ManyToManyField(LocationChoices, blank=True, verbose_name=LocationChoices._meta.verbose_name)
    living_space = models.IntegerField(_(u"Жилая площадь"), max_length=4, blank=False)
    #living_space_for_m2 = models.BooleanField(default=0,blank=True)
    total_space = models.IntegerField(_(u"Общая площадь"), max_length=4, blank=True, default="", null=True)
    #total_space_for_m2 = models.BooleanField(default=0)
    land_space = models.IntegerField(_(u"Площадь земельного участка"), max_length=4, blank=True, default="", null=True)
    #land_space_for_m2 = models.BooleanField(default=0)
    rooms_count = models.IntegerField(_(u"Количество комнат"), blank=False, default="")
    bedrooms_count = models.IntegerField(_(u"Количество спальных комнат"), blank=True, default="", null=True)
    floor = models.IntegerField(_(u"Этаж"), blank=True, default="", null=True)
    floor_type = models.ManyToManyField(FloorTypeChoices, blank=True, verbose_name=FloorTypeChoices._meta.verbose_name)
    floors_count = models.IntegerField(_(u"Этажей всего"), max_length=5, blank=True, default="", null=True)
    heating = models.ManyToManyField(HeatingOptions, blank=True)
    floor_covering = models.ManyToManyField(FloorCoveringOptions, blank=True, verbose_name=FloorCoveringOptions._meta.verbose_name)
    kitchens_count = models.IntegerField(_(u"Количество кухонь"), default="", blank=True, null=True)
    kitchen_type = models.ManyToManyField(KitchenChoices, blank=True, verbose_name=KitchenChoices._meta.verbose_name)
    bathrooms_count = models.IntegerField(_(u"Количество ванных комнат"),default="",blank=True, null=True)
    bathroom = models.ManyToManyField(BathroomChoices, blank=True, verbose_name=BathroomChoices._meta.verbose_name)
    separate_toilets_count = models.IntegerField(_(u"Количество отдельных туалетов"), default="", blank=True, null=True)
    other_facilies = models.ManyToManyField(OtherFacilitieChoices, blank=True, verbose_name=OtherFacilitieChoices._meta.verbose_name)
    security_systems = models.ManyToManyField(SecuritySystemsChoices, blank=True, verbose_name=SecuritySystemsChoices._meta.verbose_name)
    comfort = models.ManyToManyField(ComfortChoices, blank=True, verbose_name=ComfortChoices._meta.verbose_name)
    furnishings = models.ManyToManyField(FurnishingChoices, blank=True, verbose_name=FurnishingChoices._meta.verbose_name)
    additional_equipment = models.ManyToManyField(AdditionalEquipmentChoices, blank=True, verbose_name=AdditionalEquipmentChoices._meta.verbose_name)
    glazing = models.ManyToManyField(GlazingChoices, blank=True, verbose_name=GlazingChoices._meta.verbose_name)
    glass_frame = models.ManyToManyField(GlassFrameChoices, blank=True, verbose_name=GlassFrameChoices._meta.verbose_name)
    parking_count = models.IntegerField(_(u"Количество гаражей/парковочных мест"), default="", blank=True, null=True)
    #BEGIN HOW LONG GO TO ...
    dist_to_station = models.FloatField(_(u"Расстояние до вокзала"), default="", blank=True, null=True)
    dist_to_transport = models.FloatField(_(u"Расстояние до остановки общественного транспорта"), default="", blank=True, null=True)
    dist_to_airport = models.FloatField(_(u"Расстояние до аэропорта"), default="", blank=True, null=True)
    dist_to_highway = models.FloatField(_(u"Расстояние до шоссе"), default="", blank=True, null=True)
    dist_to_centre = models.FloatField(_(u"Расстояние до центра города"), default="", blank=True, null=True)
    dist_to_kindergarten = models.FloatField(_(u"Расстояние до детского сада/детской площадки"), default="", blank=True, null=True)
    dist_to_school = models.FloatField(_(u"Расстояние до нколы"), default="", blank=True, null=True)
    dist_to_university = models.FloatField(_(u"Расстояние до ВУЗа"), default="", blank=True, null=True)
    dist_to_shopping = models.FloatField(_(u"Расстояние до торгового центра"), default="", blank=True, null=True)
    dist_to_sea = models.FloatField(_(u"Расстояние до моря"), default="", blank=True, null=True)
    dist_to_beach = models.FloatField(_(u"Расстояние до пляжа"), default="", blank=True, null=True)
    dist_to_recreation = models.FloatField(_(u"Расстояние до зоны отдыха"), default="", blank=True, null=True)
    dist_to_park = models.FloatField(_(u"Расстояние до парка"), default="", blank=True, null=True)
    dist_to_slopes = models.FloatField(_(u"Расстояние до лыжной трассы"), default="", blank=True, null=True)
    dist_to_sports = models.FloatField(_(u"Расстояние до спорткомплекса"),help_text="km", default="", blank=True, null=True)
    #END HOW LONG GO TO ...eeeeeeuuuuhhhh
    window_view = models.ManyToManyField(WindowViewChoices, blank=True, verbose_name=WindowViewChoices._meta.verbose_name)
    historical_monument = models.BooleanField(_(u"Охраняется как исторический памятник"), default=0)
    possible_redevelopment = models.BooleanField(_(u"Возможна перепланировка"), default=0)
    condition = models.ManyToManyField(ConditionChoices, blank=True, verbose_name=ConditionChoices._meta.verbose_name)
    description = models.TextField(_(u"Описание"), blank=True, null=True) # All languages
    object_location = models.TextField(_(u"Расположение объекта"), blank=True, null=True) # All languages
    created = models.DateTimeField(_(u"Создано"), auto_now_add=True)
    updated = models.DateTimeField(_(u"Обновлено"), auto_now=True)
    views = models.IntegerField(_(u"Просмотры"), default=0, blank=True, null=True)

    def __unicode__(self):
        return  unicode(self.name)

    def  __str__(self):
        return self.__unicode__()

    @property
    def is_new(self):
        import datetime
        delta = datetime.timedelta(hours=24*14)
        if self.created > datetime.datetime.today() - delta:
            return True
        return False

    def save(self, *args, **kwargs):
    #    self.name = self.name_ru
    #    self.description = self.description_ru
    #    self.object_location = self.object_location_ru

        #0 - Search Only
        #1 - Search And Students
        #2 - Students Only

        if self.for_students == True and self.only_for_students == True:
            self.students = 1
        if self.for_students == False and self.only_for_students == False:
            self.students = 0
        if self.for_students == True and self.only_for_students == False:
            self.students = 1
        if self.for_students == False and self.only_for_students == True:
            self.students = 2

        super(Apartament, self).save()
        # When create apartment - create dir to upload files
        path = settings.MEDIA_ROOT + 'uploads/%s/%s/' % (self.user.id, self.id) 
        if not os.path.isdir(path):
            os.makedirs(path)

    class Meta:
        ordering = ('-created')

    def get_fields_list(self):
        '''
        Deprecated
        '''
        list = [(field) for field in self._meta.fields]
        exclude = ['id','created','updated']
        include = []
        for k in list:
            if k.get_attname() not in exclude:
                include.append(str(k.get_attname()))
        return include

    def main_image(self):
        ''' Get image to be displayed in lists '''
        result = self.photo_set.filter()[:1]
        for i in result:
            return i

    class Meta:
        verbose_name = _(u"Недвижимость")
        verbose_name_plural = _(u"Недвижимость")

class Bookmarks(models.Model):
    apartment = models.ForeignKey(Apartament)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = _(u"Закладка")
        verbose_name_plural = _(u"Закладки")

class Document(models.Model):
    apartament = models.ForeignKey(Apartament)
    file_name = models.FileField(upload_to='uploads/')

    def get_url(self):
        return settings.MEDIA_URL + '/' + str(self.file_name)
       
    def icon_url(self): 
        return "/media/design/images/icons/%s.png" % str(self.file_name).split(".")[-1]

    class Meta:
        verbose_name = _(u"Документ")
        verbose_name_plural = _(u"Документы")

class Photo(models.Model):
    apartament = models.ForeignKey(Apartament)
    photo = models.ImageField(upload_to='uploads/')

    def get_image_url(self):
        return settings.MEDIA_URL + '/' + str(self.photo)

    def save(self, *args, **kwargs):
        # When upload new image, we'll resize it.
        if not self.id:
            full_path = os.path.realpath(settings.MEDIA_ROOT + str(self.photo))
            img = Image.open(full_path)

            src_width, src_height = img.size

            if src_width > settings.MAX_IMAGE_WIDTH and src_height > settings.MAX_IMAGE_HEIGHT:
                src_ratio = float(src_width) / float(src_height)
                dst_width, dst_height = settings.MAX_IMAGE_WIDTH, settings.MAX_IMAGE_HEIGHT
                dst_ratio = float(dst_width) / float(dst_height)

                if dst_ratio < src_ratio:
                    crop_height = src_height
                    crop_width = crop_height * dst_ratio
                    x_offset = float(src_width - crop_width) / 8
                    y_offset = 0
                else:
                    crop_width = src_width
                    crop_height = crop_width / dst_ratio
                    x_offset = 0
                    y_offset = float(src_height - crop_height) / 15
                img = img.crop((int(x_offset), int(y_offset), int(x_offset)+int(crop_width), int(y_offset+int(crop_height))))
                img = img.resize((dst_width, dst_height), Image.ANTIALIAS)

                img.save(full_path, "JPEG", quality=settings.UPLOAD_IMAGE_QUALITY)

        super(Photo, self).save(*args,**kwargs)

    class Meta:
        verbose_name = _(u"Изображение")
        verbose_name_plural = _(u"Изображения")

class EstateTypeSeoText(models.Model):
    type_id = models.CharField(max_length=100, blank = False, choices=ESTATE_TYPE_CHOICES)
    country = models.ForeignKey(Country, blank=False, default=0)
    description = models.TextField(_(u"Описание"), blank=True, null=True)

    def __unicode__(self):
        return self.type_id
