# -*- coding: utf-8 -*-
import time
import hashlib
import string

from django.utils.translation import ugettext_lazy as _
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from users.models import UserProfile
from tarifs.models import Tarif, TarifRequests

hexchars="0123456789ABCDEF"

# Compare this to its 'c' equivalent in bin2hex.c...
def dit2hex(ch):
    i=ord(ch) # get its integral value.
    leftnib=i>>4
    rightnib=i & 0xf
    leftchar=hexchars[leftnib]
    rightchar=hexchars[rightnib]
    return leftchar+rightchar

# compare this to its 'c' equivalent in bin2hex.c...
def bin2hex(str):
    retvalue=""  # return value is empty until we add to it...
    for s in str:
        hexchars=dit2hex(s)
        retvalue=retvalue+hexchars
        pass
    return retvalue

@login_required()
def index(request):
    ''' Display table with tarifs
    '''
    # Check if user is saler
    user_profile = get_object_or_404(UserProfile, user=request.user, is_saler=True)

    # get current tarif
    try:
        current_tarif = TarifRequests.objects.get(user=user_profile)
    except:
        current_tarif = None

    model = Tarif.objects.all()
    return direct_to_template(request, 'tarifs/index.html', {
        'model': model,
        'current_tarif': current_tarif,
    })

@login_required()
def select_tarif(request):
    '''
        Select tarif. Send request to admin and show pay page.
    '''
    get_object_or_404(UserProfile, user=request.user, is_saler=True)

    tid =  request.POST.get('tarif_id', 0)

    if tid == 0:
        tid = 4

    tarif = get_object_or_404(Tarif, pk=int(tid))
             
    monthes = int(request.POST.get('monthes', 1))
    sum = tarif.price * monthes

    import datetime
    from datetime import timedelta

    now = datetime.datetime.now()
    diff = datetime.timedelta(days=93)
    future = now + diff

    if tarif.price == 0:
        user_profile = get_object_or_404(UserProfile, user=request.user, is_saler=True)
        tarif_request = TarifRequests(
            user = user_profile,
            tarif = tarif,
            months_count = monthes,
            paid = True,
            start_date = datetime.date.today().isoformat(),
            end_date = future.strftime("%Y-%m-%d")
        )
        tarif_request.save() 
        messages.success(request, _(u"Тариф активирован"))
        return redirect('/estates/cart')

    return  direct_to_template(request, 'tarifs/select.html', {
        'tarif': tarif,
        'monthes': monthes,
        'sum': sum,
    })

@login_required()
def confimed(request):
    user_profile = get_object_or_404(UserProfile, user=request.user, is_saler=True)

    tarif = get_object_or_404(Tarif, pk=int(request.POST.get('tarif_id',0)))
    monthes = int(request.POST.get('monthes', 1))
    sum = tarif.price * monthes

    tarif_request = TarifRequests(
        user = user_profile,
        tarif = tarif,
        months_count = monthes,
    )
    tarif_request.save()
    return redirect('tarif-paypage')

@login_required()
def show_pay_page(request):
    user_profile = get_object_or_404(UserProfile, user=request.user, is_saler=True)

    tarif_request = TarifRequests.objects.get(user=user_profile)
    sum = str(tarif_request.tarif.price * tarif_request.months_count)
    
    txndatetime = time.strftime("%Y:%m:%d-%H:%M:%S") 
    payment_data = {
        'storename': 1292933401, 
        'txndatetime': txndatetime,
        'chargetotal': sum,
        'currency': '978',
        'sharedsecret': 'x2fj9xBX6p',
    }

    hash_str = "%s%s%s%s%s" % (
        payment_data['storename'],
        payment_data['txndatetime'],
        payment_data['chargetotal'],
        payment_data['currency'],
        payment_data['sharedsecret'],
    )

    print hashlib.sha1(bin2hex(hash_str).lower()).hexdigest()

    return direct_to_template(request, 'tarifs/confirmed.html', {
        'tarif_request':tarif_request,
        'sum': sum,
        'txndatetime': txndatetime,
        'hash': hashlib.sha1(bin2hex(hash_str).lower()).hexdigest().lower(),
    })

@login_required()
def cancel_request(request):
    user_profile = get_object_or_404(UserProfile, user=request.user, is_saler=True)
    TarifRequests.objects.filter(user=user_profile, paid=False).delete()
    return redirect('choose-tarif')

