# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    ''' For to send messages from /contacts page '''
    #def __init__(self, *args, **kwargs):
    #    super(ContactForm, self).__init__(*args, **kwargs)
    #    self.fields['first_name'].initial = "privet"

    first_name = forms.CharField(label=_(u"Имя"))
    last_name = forms.CharField(label=_(u"Фамилия"), required=False)
    phone = forms.CharField(required=False,label=_(u"Телефон"))
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(),label=_(u"Сообщение"))

class WeWillRecallYouForm(forms.Form):
    ''' Used from /contacts page '''
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    time = forms.CharField()
    theme = forms.CharField(widget=forms.Textarea())
