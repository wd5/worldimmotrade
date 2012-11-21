# -*- coding: utf-8 -*-
# Users app forms
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.text import get_text_list, capfirst

from users.models import UserProfile
from world.models import Country, Region, City

class SalerRegisterForm(forms.ModelForm):
    """ Saler register form """
    def __init__(self,*args, **kwargs):
        request = kwargs.pop('request', None)
        super(SalerRegisterForm, self).__init__(*args, **kwargs)
        self.fields['country'].label = capfirst(_(u"Страна"))
        self.fields['region'].label = capfirst(_(u"Регион"))
        self.fields['city'].label = capfirst(_(u"Город"))
        if self.instance is None and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=0)
            self.fields['city'].queryset = City.objects.filter(region=0)
        if self.instance.id and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.instance.country)
            self.fields['city'].queryset = City.objects.filter(region=self.instance.region)
        if len(self.data) > 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.data.get('country') or 0)
            self.fields['city'].queryset = City.objects.filter(region=self.data.get('region') or 0)

        host = request.get_host()
        if host.endswith('.com'):
            self.fields['country'].queryset = Country.objects.order_by('name_en').all()
        if host.endswith('.de'):
            self.fields['country'].queryset = Country.objects.order_by('name_de').all()
        if host.endswith('.ru'):
            self.fields['country'].queryset = Country.objects.order_by('name_ru').all()
        
    company_name = forms.CharField(label=capfirst(_(u"Название фирмы")), required=True, max_length=255)
    mobile_phone = forms.CharField(label=capfirst(_(u"Мобильный телефон")), required=False, max_length=30)
    fax_number = forms.CharField(label=capfirst(_(u"Номер факса")), required=False, max_length=30)
    password = forms.CharField(label=capfirst(_(u"Пароль")), required=True,widget=forms.PasswordInput(), min_length=4, max_length=30)
    repeat_password = forms.CharField(label=capfirst(_(u"Повторите пароль")), required=True, widget=forms.PasswordInput(), min_length=4,max_length=30)
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    region = forms.ModelChoiceField(queryset=Region.objects.filter(id=0))
    city = forms.ModelChoiceField(queryset=Region.objects.filter(id=0))

    def clean_repeat_password(self):
        confirm_password = self.cleaned_data['repeat_password']
        original_password = self.cleaned_data['password']
        if original_password != confirm_password:
            raise forms.ValidationError(_(u"Занчения Пароль и Повторите пароль должны совпадать."))

        return confirm_password

    class  Meta:
        model = UserProfile
        exclude = ['user', 'is_saler']

class UserRegisterForm(forms.ModelForm):
    """ User register form """
    mobile_phone = forms.CharField(label=capfirst(_(u"Мобильный телефон")), required=True, max_length=30)
    fax_number = forms.CharField(label=capfirst(_(u"Номер факса")), required=False, max_length=30)
    password = forms.CharField(label=capfirst(_(u"Пароль")), required=True,widget=forms.PasswordInput(), min_length=4, max_length=30)
    repeat_password = forms.CharField(label=capfirst(_(u"Повторите пароль")), required=True, widget=forms.PasswordInput(), min_length=4,max_length=30)

    def clean_repeat_password(self):
        confirm_password = self.cleaned_data['repeat_password']
        original_password = self.cleaned_data['password']
        if original_password != confirm_password:
            raise forms.ValidationError(capfirst(_(u"Занчения Пароль и Повторите пароль должны совпадать.")))

        return confirm_password

    class  Meta:
        model = UserProfile
        exclude = ['user', 'is_saler', 'country', 'region', 'city', 'company_name', 'address', 'post_code', 'personal_info_show']
        fields = ['treatment','first_name', 'last_name', 'phone', 'mobile_phone', 'fax_number', 'contact_lang','email', 'receive_mails']

# For profile edit mode
class SalerEditForm(forms.ModelForm):
    """ Saler register form """
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(SalerEditForm, self).__init__(*args, **kwargs)
        self.fields['country'].label = capfirst((u"Страна"))
        self.fields['region'].label = capfirst((u"Регион"))
        self.fields['city'].label = capfirst((u"Город"))

        host = request.get_host()
        if host.endswith('.com'):
            self.fields['country'].queryset = Country.objects.order_by('name_en').all()
        if host.endswith('.de'):
            self.fields['country'].queryset = Country.objects.order_by('name_de').all()
        if host.endswith('.ru'):
            self.fields['country'].queryset = Country.objects.order_by('name_ru').all()
        
        if self.instance is None and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=0)
            self.fields['city'].queryset = City.objects.filter(region=0)
        if self.instance.id and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.instance.country)
            self.fields['city'].queryset = City.objects.filter(region=self.instance.region)
        if len(self.data) > 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.data.get('country') or 0)
            self.fields['city'].queryset = City.objects.filter(region=self.data.get('region') or 0)

    company_name = forms.CharField(label=capfirst(_(u"Название фирмы")), required=True, max_length=255)
    mobile_phone = forms.CharField(label=capfirst(_(u"Мобильный телефон")), required=False, max_length=30)
    fax_number = forms.CharField(label=capfirst(_(u"Номер факса")), required=False, max_length=30)
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    region = forms.ModelChoiceField(queryset=Region.objects.filter(id=0))
    city = forms.ModelChoiceField(queryset=Region.objects.filter(id=0))

    class  Meta:
        model = UserProfile
        exclude = ['user', 'is_saler', 'email']

# For profile edit mode
class UserEditForm(forms.ModelForm):
    """ User register form """
    mobile_phone = forms.CharField(label=capfirst(_(u"Мобильный телефон")), required=True, max_length=30)
    fax_number = forms.CharField(label=capfirst(_(u"Номер факса")), required=False, max_length=30)

    class  Meta:
        model = UserProfile
        exclude = ['user', 'is_saler', 'country', 'region', 'city', 'company_name', 'address', 'post_code', 'personal_info_show','email']
        fields = ['treatment','first_name', 'last_name', 'phone', 'mobile_phone', 'fax_number', 'receive_mails']


class LoginForm(forms.Form):
    """ Form for login users """
    email = forms.EmailField(label=capfirst(_(u"E-Mail")), min_length=4)
    password = forms.CharField(label=capfirst(_(u"Пароль")), min_length=4, max_length=30, widget=forms.PasswordInput())

    
