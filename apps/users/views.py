# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, \
    login as auth_login, \
    logout as auth_logout
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from users.models import UserProfile
from users.forms import *


def choose_type(request):
    return direct_to_template(request, 'users/choose_type.html')


def register(request, saler):
    """
    Here we register new users, salers and users
    saler: determinates what type of user we registering
    """
    if request.user.is_authenticated():
        return redirect('/')

    if saler == True:
        form = SalerRegisterForm(request.POST or None, request=request)
    else:
        form = UserRegisterForm(request.POST or None)
	
    if form.is_valid():
        try:
            User.objects.get(email__exact=form.cleaned_data['email'])
            form._errors['email'] = form.error_class([_(u'Пользователь с таким адресом уже зарегестрирован в системе')])
        except User.DoesNotExist:
            # Register new user
            user = User.objects.create_user(form.cleaned_data['email'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            # Create new user
            form = form.save(commit=False)
            form.user = user
            form.is_saler = saler
            form.save()

            if request.POST['treatment'] == 'mr':
                mr_or_mrs = 'Уважаемый'
            else:
                mr_or_mrs = 'Уважаемая'

            message = render_to_string('emails/reg.html', {'email': request.POST['email'], 'mr_or_mrs':mr_or_mrs})
            email = EmailMessage(_(u"worldimmotrade.com"), message, settings.ROBOT_EMAIL, [request.POST['email']])
            email.content_subtype = "html"
            email.send()

            auth_user = authenticate(username=request.POST['email'], password=request.POST['password'])
            if auth_user is not None:
                if auth_user.is_active:
                    auth_login(request, auth_user)
                    return redirect('/estates/list/')
            return  redirect('users-thanks')

    return direct_to_template(request, 'users/register.html', {
        'form': form,
        'saler': saler,
    })

def login(request):
    """ Login user """
    if request.user.is_authenticated():
        return redirect('/')

    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('/estates/list/')
            else:
                form._errors['email'] = form.error_class([_(u'Вас забанили')])
        else:
            form._errors['email'] = form.error_class([_(u'Ошибка авторизации. Пользователь не найден.')])

    return direct_to_template(request,'users/login.html', {
        'form': form,
    })

def logout(request):				
	""" Logout authenticated user """
	if request.user.is_authenticated():
		auth_logout(request)
	return redirect('/')

def thanks(request):
    """ Show OK after register """
    return direct_to_template(request, 'users/thanks.html',{})

@login_required()
def edit_profile(request):
    ''' Edit user profile '''
    profile = get_object_or_404(UserProfile, user=request.user)
	
    if profile.is_saler == True:
        form = SalerEditForm(request.POST or None, instance=profile, request=request)
    else:
        form = UserEditForm(request.POST or None, instance=profile)

    if form.is_valid():
        messages.success(request, _(u"Изменения сохранены."))
        form.save()

    return direct_to_template(request, 'users/edit_profile.html', {
        'form': form
    })

def change_currency(request):
    currency = request.POST.get("currency")
    request.session['current_currency'] = currency
    return redirect(request.POST.get('redirect', '/'))

def companiesList(request):
    '''
        Display companies list
    '''

    models = UserProfile.objects.all()
    for m in models:
        try:
            m.company_name = m.company_name.strip()
            m.save()
        except:
            pass

    models = UserProfile.objects.filter(company_name__isnull=False, is_saler=True, personal_info_show='full').exclude(company_name='-').order_by('company_name')
    paginator = Paginator(models, settings.OBJECTS_PER_PAGE)

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        models = paginator.page(page)
    except (EmptyPage, InvalidPage):
        models = paginator.page(paginator.num_pages)

    return direct_to_template(request, 'users/companies.html', {
        'models': models,
        'per_page': settings.OBJECTS_PER_PAGE,        
    })

