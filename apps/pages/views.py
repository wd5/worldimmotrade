# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.shortcuts import HttpResponse

from pages.models import StaticPage, News, CountryInfo
from pages.forms import *
from estates.forms import SearchForm
from tarifs.models import Tarif


def show_page(request, slug):
    ''' Display static page '''
    model = get_object_or_404(StaticPage, url = slug)
    return direct_to_template(request, 'static_page.html',{
        'model': model,
        'search_form': SearchForm()
    })

def show_news_page(request, id):
    ''' Dispaly news page '''
    model = get_object_or_404(News, pk = id)
    return direct_to_template(request, 'news_page.html',{
        'model': model,
        'search_form': SearchForm()
    })

def show_all_news(request):
    ''' Display all news '''
    news_list =News.objects.all()
    paginator = Paginator(news_list, settings.OBJECTS_PER_PAGE)

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        news_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        news_list = paginator.page(paginator.num_pages)

    return direct_to_template(request, 'news_list.html', {
        'news_list': news_list,
        'per_page': settings.OBJECTS_PER_PAGE,
        'search_form': SearchForm()
    })

def contacts(request):
    ''' Display contacts and "we-will-recall-you" form '''
    # Process contact form
    if request.POST.get('send_contact', False):
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            # Send email
            message = render_to_string('emails/contact.html',contact_form.cleaned_data)
            email = EmailMessage(_(u"Сообщение из страницы контактов"), message, settings.ROBOT_EMAIL, [settings.CONTACTS_EMAIL])
            email.content_subtype = "html"
            email.send()

            return redirect('view-contacts')
    else:
        contact_form = ContactForm()

    # Process recall form
    if request.POST.get('send_recall', False):
        recall_form = WeWillRecallYouForm(request.POST or None)
        if recall_form.is_valid():
            # Send email
            message = render_to_string('emails/recall.html',recall_form.cleaned_data)
            email = EmailMessage(_(u"Прозьба перезвонить"), message, settings.ROBOT_EMAIL, [settings.CONTACTS_EMAIL])
            email.content_subtype = "html"
            email.send()

            return redirect('view-contacts')
    else:
        recall_form = WeWillRecallYouForm()

    return direct_to_template(request, 'contacts.html', {
        'contact_form': contact_form,
        'recall_form': recall_form,
        'search_form': SearchForm()
    })

def organisation(request):
    if request.POST.get('send_contact', False):
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            # Send email
            message = render_to_string('emails/contact.html',contact_form.cleaned_data)
            email = EmailMessage(_(u"Сообщение из страницы контактов"), message, settings.ROBOT_EMAIL, [settings.CONTACTS_EMAIL])
            email.content_subtype = "html"
            email.send()

            return redirect('/page/organisation/')
    else:
        contact_form = ContactForm()

    return direct_to_template(request, 'pages/organisation.html', {
        'contact_form': contact_form,
    })

def show_country_info(request, country_id):
    model = get_object_or_404(CountryInfo, country=country_id)
    return direct_to_template(request, "pages/country_info.html", {
        'model':model,
        'data':{'show_country_info':True},
    })

def iframe_page(request, name):
    return direct_to_template(request,'iframes/all.html',{
        'name':name
    })


def convert(request):
    from annoing.currencyManager import currencyManager
    manager = currencyManager()
    from_c = request.GET.get('from_c')

    try:
        sum = int(request.GET.get('sum'))
    except:
        sum = 1

    process = {
     'R01720': 'UAH',
     'R01235': 'USD',
     'RUBLES': 'RUR',
     'R01035': 'GPB',
     'R01239': 'EUR',
    }

    html_response = '<ul>'
    for k in process:
        result = round(manager.convert(from_c=from_c, to_c=k, sum=sum), 2)
        html_response += "<li><em>%s</em><span>%s</span></li>" % (result, process[k])

    return HttpResponse(html_response + '</ul>')

def pricing(request):
    return direct_to_template(request, "pages/pricing.html", {
        'model': Tarif.objects.all()
    })
