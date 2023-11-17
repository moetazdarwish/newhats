import json
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timezone

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from customers.models import CustomerProfile, BusinessUnit
from whatsapp.cartaction import *
from whatsapp.messagecreation import *
from whatsapp.models import *


def sendTextMsg(phone, message):
    url = 'https://graph.facebook.com/v17.0/160030170524038/messages/'

    headers = {
        'Authorization': 'Bearer EAAx3hZAqlPmMBO3hCyAZALgeJjhj3zlnqJ3OTIFTcLBjmLiwyw9p7qtwNZCaphKUbomLUvtz1poBPTyI5iZAaRv5ZCTJT9qHKAbOxG1RPbZBydyf3duByJEiGOE0Hk9pt5JDqojYcIrFjOHFXZAaTzOJ35c5nlNZAZBXdsDMogqm9XXO3BceZC1kIBkdCcQuWjtTwEfUitj8XxU4nriBMLDRiA1WKBFu0ZD'}
    payload = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': phone,
        "type": "text",
        'text': {'body': message}
    }
    print(message)
    # response = requests.post(url=url,headers=headers,json=payload)
    # ans = response.json()
    # print(ans)
    return (message)
def sendInteractivMsg(phone, message, btn):
    url = 'https://graph.facebook.com/v17.0/160030170524038/messages/'

    headers = {
        'Authorization': 'Bearer EAAx3hZAqlPmMBO3hCyAZALgeJjhj3zlnqJ3OTIFTcLBjmLiwyw9p7qtwNZCaphKUbomLUvtz1poBPTyI5iZAaRv5ZCTJT9qHKAbOxG1RPbZBydyf3duByJEiGOE0Hk9pt5JDqojYcIrFjOHFXZAaTzOJ35c5nlNZAZBXdsDMogqm9XXO3BceZC1kIBkdCcQuWjtTwEfUitj8XxU4nriBMLDRiA1WKBFu0ZD'}
    payload = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': phone,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": message
            },
            "action": {
                "buttons": btn

            }
        }
    }
    msg = json.dumps(payload, ensure_ascii=False)
    print(msg)
    # response = requests.post(url=url,headers=headers,json=payload)
    # ans = response.json()
    # print(ans)
    return (msg)
def sendListMsg(phone, txt1, txt2,txt3,lst):
    url = 'https://graph.facebook.com/v17.0/160030170524038/messages/'

    headers = {
        'Authorization': 'Bearer EAAx3hZAqlPmMBO3hCyAZALgeJjhj3zlnqJ3OTIFTcLBjmLiwyw9p7qtwNZCaphKUbomLUvtz1poBPTyI5iZAaRv5ZCTJT9qHKAbOxG1RPbZBydyf3duByJEiGOE0Hk9pt5JDqojYcIrFjOHFXZAaTzOJ35c5nlNZAZBXdsDMogqm9XXO3BceZC1kIBkdCcQuWjtTwEfUitj8XxU4nriBMLDRiA1WKBFu0ZD'}
    payload = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': phone,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": txt1
            },

            "action": {
                "button": txt2,
                "sections": [
                    {
                        "title": txt3,
                        "rows": lst
                    },
                ]
            }
        }
    }
    msg = payload
    print(msg)
    # response = requests.post(url=url,headers=headers,json=payload)
    # ans = response.json()
    # print(ans)
    return (msg)
def sendLocationMsg(phone, long, lat,name,add):
    url = 'https://graph.facebook.com/v17.0/160030170524038/messages/'

    headers = {
        'Authorization': 'Bearer EAAx3hZAqlPmMBO3hCyAZALgeJjhj3zlnqJ3OTIFTcLBjmLiwyw9p7qtwNZCaphKUbomLUvtz1poBPTyI5iZAaRv5ZCTJT9qHKAbOxG1RPbZBydyf3duByJEiGOE0Hk9pt5JDqojYcIrFjOHFXZAaTzOJ35c5nlNZAZBXdsDMogqm9XXO3BceZC1kIBkdCcQuWjtTwEfUitj8XxU4nriBMLDRiA1WKBFu0ZD'}
    payload = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': phone,
        "type": "location",
          "location": {
            "longitude": long,
            "latitude": lat,
            "name": name,
            "address": add
          }
    }
    msg = json.dumps(payload, ensure_ascii=False)
    print(msg)
    # response = requests.post(url=url,headers=headers,json=payload)
    # ans = response.json()
    # print(ans)
    return (msg)
def sendProductMsg(phone, message):
    url = 'https://graph.facebook.com/v17.0/160030170524038/messages/'

    headers = {
        'Authorization': 'Bearer EAAx3hZAqlPmMBO3hCyAZALgeJjhj3zlnqJ3OTIFTcLBjmLiwyw9p7qtwNZCaphKUbomLUvtz1poBPTyI5iZAaRv5ZCTJT9qHKAbOxG1RPbZBydyf3duByJEiGOE0Hk9pt5JDqojYcIrFjOHFXZAaTzOJ35c5nlNZAZBXdsDMogqm9XXO3BceZC1kIBkdCcQuWjtTwEfUitj8XxU4nriBMLDRiA1WKBFu0ZD'}
    payload = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': phone,
        "type": "interactive",
        "interactive": message
    }
    msg = json.dumps(payload, ensure_ascii=False)
    print(msg)
    # response = requests.post(url=url,headers=headers,json=payload)
    # ans = response.json()
    # print(ans)
    return (msg)

# @csrf_exempt
@api_view(['GET','POST'])
def recievingWhatsApp(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        # pricing = data['entry'][0]['changes'][0]['value']['statuses'][0]['pricing']['billable']
        # wamid = data['entry'][0]['changes'][0]['value']['statuses'][0]['id']
        # conversation = data['entry'][0]['changes'][0]['value']['statuses'][0]['conversation']['id']
        #

        type = data['entry'][0]['changes'][0]['value']['messages'][0]['type']
        acc_num = data['entry'][0]['changes'][0]['value']['metadata']['display_phone_number']
        phone_num = data['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
        get_busine = BusinessUnit.objects.get(phone=acc_num)
        business_type = get_busine.cat.id
        reslt='n/a'
        if 'messages' in data['entry'][0]['changes'][0]['value']:
            print('helllo')
        if 'statuses' in data['entry'][0]['changes'][0]['value']:
            print('kfj')
        if type == 'text':
            text = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            print(text)
            language = checkConver(phone_num, get_busine)
            chkk = checkTxt(phone_num, get_busine, text)
            textmaping(phone_num, get_busine)
            if chkk:
                if business_type == 1:
                    reslt = productMaping(phone_num, get_busine, text)
                if business_type == 2:
                    reslt = serviceMaping(phone_num, get_busine, text)
                if business_type == 'simple':
                    reslt = simpleMaping(phone_num, get_busine, text)
                if business_type == 5:
                    reslt = clinicMaping(phone_num, get_busine, text)
            else:
                reslt = chkk
        elif type == 'location':
            long = data['entry'][0]['changes'][0]['value']['messages'][0]['location']['longitude']
            latitude = data['entry'][0]['changes'][0]['value']['messages'][0]['location']['latitude']
            locationAction(phone_num, long, latitude)
            if business_type == 1:
                reslt = productMaping(phone_num, get_busine, 'location')
        elif type == 'interactive':
            btn_type = data['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['type']
            if btn_type == 'button_reply':
                btn_id = data['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['button_reply']['id']
                btn_txt = data['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['button_reply']['title']
                if business_type == 1:
                    interactiveAction(phone_num, btn_id, get_busine)
                    reslt = productMaping(phone_num, get_busine, btn_txt)
                if business_type == 2:
                    interServiceAction(phone_num, btn_id, get_busine)
                    reslt = serviceMaping(phone_num, get_busine, btn_txt)
                if business_type == 'simple':
                    interSimpleAction(phone_num, btn_id, get_busine)
                    reslt = simpleMaping(phone_num, get_busine, btn_txt)
                if business_type == 5:
                    clinicAction(phone_num, btn_id, get_busine)
                    reslt = clinicMaping(phone_num, get_busine, btn_txt)
            if btn_type == 'list_reply':
                btn_id = data['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['list_reply']['id']
                btn_txt = data['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['list_reply']['title']
                if business_type == 1:
                    interactiveAction(phone_num, btn_id, get_busine)
                    reslt = productMaping(phone_num, get_busine, btn_txt)
                if business_type == 2:
                    interServiceAction(phone_num, btn_id, get_busine)
                    reslt = productMaping(phone_num, get_busine, btn_txt)
                if business_type == 5:
                    clinicAction(phone_num, btn_id, get_busine)
                    reslt = clinicMaping(phone_num, get_busine, btn_txt)
        return HttpResponse(reslt)
        # return HttpResponse ('rst',status=200)

    if request.method == 'GET':
        mode = request.query_params['hub.mode']
        challenge = request.query_params['hub.challenge']
        token = request.query_params['hub.verify_token']
        return HttpResponse(challenge, status=200)


def cheklasttime(time1):
    now = datetime.now(timezone.utc)
    chk = (now - time1)
    chk = chk.total_seconds()
    time = chk / 60
    if time > 60:
        return False
    return True
def checkTxt(phone, business, txt):
    txt = txt.lower()
    obj_name = CustomerProfile.objects.get(phone=phone)
    conv = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    step = conv.step
    if txt == '0':
        conv.status = 'CANCELED'
        conv.save()
        if business.cat.id == 1:
            WhatsMsg.objects.create(name=obj_name, business=business, step=3, status='CREATED')
            return True
        if business.cat.id == 2:
            WhatsMsg.objects.create(name=obj_name, business=business, step=50, status='CREATED')
            return True
    if  step == 1 or step == 2 or step == 15 or step == 21 or step == 23 :
        if len(txt) >= 1:
            return True
    if step == 3:
        obj_name.name = txt
        obj_name.save()
        conv.step = 4
        conv.save(update_fields=['step'])
        return True
    if step == 82:
        obj_name.name = txt
        obj_name.save()
        conv.step = 83
        conv.save(update_fields=['step'])
        return True

    if step == 52:
        obj_name.name = txt
        obj_name.save()
        conv.step = 53
        conv.save(update_fields=['step'])
        return True
    return True


    # else:
    #     obj = WhatsMsgConve.objects.create(con_name=conv, msg=txt, step=step)
    #     message = textMessage(30, '', obj, conv.lang)
    #     action = sendTextMsg(phone, message)
    #     return action

def checkConver(phone, business):
    try:
        obj_name = CustomerProfile.objects.get(phone=phone)
        try:
            conv = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
            chk = cheklasttime(conv.date)
            if chk:
                return True
            conv.status = 'CLOSED'
            conv.save()
            WhatsMsg.objects.create(name=obj_name, business=business, status='CREATED')
            return 'action'
        except:
            WhatsMsg.objects.create(name=obj_name, business=business, status='CREATED')
            return 'action'
    except:
        obj_name = CustomerProfile.objects.create(phone=phone)
        WhatsMsg.objects.create(name=obj_name, business=business, status='CREATED')
        return 'action',
def locationAction(phone, Long, lat):
    obj_name = CustomerProfile.objects.get(phone=phone)
    obj_name.latitude = lat
    obj_name.longitude = Long
    obj_name.save(update_fields=['latitude', 'longitude'])
    return True
def checkCustomer(phone):
    obj_name = CustomerProfile.objects.get(phone=phone)
    if obj_name.name:
        return True
    return False
def textmaping(phone, business):
    obj_name = CustomerProfile.objects.get(phone=phone)
    conv = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    business_type = business.cat.id
    if conv.step == 1:
        if business_type == 1:
            if business.extlang:
                return True
            chk_nam = checkCustomer(phone)
            if chk_nam:
                conv.lang = business.lang
                conv.step = 4
                conv.save(update_fields=['lang', 'step'])
                return True
            conv.lang = business.lang
            conv.step = 1
            conv.save(update_fields=['lang', 'step'])
            return True
        if business_type == 2:
            if business.extlang:
                conv.step = 50
                conv.save(update_fields=[ 'step'])
                return True
            chk_nam = checkCustomer(phone)
            if chk_nam:
                conv.lang = business.lang
                conv.step = 53
                conv.save(update_fields=['lang', 'step'])
                return True
            conv.lang = business.lang
            conv.step = 51
            conv.save(update_fields=['lang', 'step'])
            return True
        if business_type == 5:
            if business.extlang:
                conv.step = 80
                conv.save(update_fields=['step'])
                return True
            chk_nam = checkCustomer(phone)
            if chk_nam:
                conv.lang = business.lang
                conv.step = 83
                conv.save(update_fields=['lang', 'step'])
                return True
            conv.lang = business.lang
            conv.step = 81
            conv.save(update_fields=['lang', 'step'])
            return True

# Product 2 Category

def interactiveAction(phone, btn, business):
    obj_name = CustomerProfile.objects.get(phone=phone)
    conv = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    rply = WhatsMsgReply.objects.get(id=btn)

    if rply.step == 1:
        chk_nam = checkCustomer(phone)
        if chk_nam:
            lg = 1
            if rply.serial != "1":
                lg = business.lang
            conv.step = 4
            conv.lang = lg
            conv.save(update_fields=['lang', 'step'])
            return True
        lg = 1
        if rply.serial != "1":
            lg = business.lang
        conv.lang = lg
        conv.step = 3
        conv.save(update_fields=['lang', 'step'])
        return True

    if rply.step == 4:
        row = WhatsTempMsg.objects.get(id=rply.serial)
        conv.step = row.next
        conv.save(update_fields=['step'])
        return False
    if rply.step == 5:
        conv.step = 6
        conv.flt = rply.serial
        conv.save(update_fields=['step', 'flt'])
        return False

    if rply.step == 6:
        row = WhatsTempMsg.objects.get(id=rply.serial)
        conv.step = row.next
        conv.save(update_fields=['step'])
        return False
    if rply.step == 7:
        row = WhatsTempMsg.objects.get(id=rply.serial)
        conv.step = row.next
        conv.save(update_fields=['step'])
        return False
    if rply.step == 8:
        conv.step = 13
        conv.extr = rply.serial
        conv.save(update_fields=['step', 'extr'])
        return False

    if rply.step == 14:

        row = WhatsTempMsg.objects.get(id=rply.serial)
        print(row.next)
        conv.step = row.next
        conv.save(update_fields=['step'])
        return False
    if rply.step == 16:
        if rply.extr == 'CRF':
            if obj_name.address:
                conv.step = 18
                conv.save(update_fields=['step'])
                return False
            conv.step = 21
            conv.save(update_fields=['step'])
            return False
        if rply.extr == 'DET':
            conv.step = 19
            conv.save(update_fields=['step'])
            return False
    if rply.step == 26:
        conv.step = 27
        conv.extr = rply.serial
        conv.save(update_fields=['step', 'extr'])
        return False
def productMaping(phone, business, txt):
    obj_name = CustomerProfile.objects.get(phone=phone)
    conversation = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    position = conversation.step
    lang = conversation.lang
    restp = conversation.flt
    mroe = conversation.extr
    if position == 1:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=1)
        message = textMessage(position, business.name, obj, lang)
        btn = interactionCreation(position, obj, business, lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 2:
        conversation.step = 3
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, business.name, obj,business.lang)
        action = sendTextMsg(phone, message)
        message2 = textMessage(3, business.name, obj, lang)
        action2 = sendTextMsg(phone, message2)
        return action

    if position == 3:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, business.name, obj, lang)
        action = sendTextMsg(phone, message)
        return action

    if position == 4:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, obj_name.name, obj, lang)

        btn = interactionCreation(position, obj, business, lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 5:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        btn = interactionCreation(position, obj, business, lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 6:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = filterListCreation(position, obj, business, lang)
        action = sendListMsg(phone, message[0], message[1], message[2], message[3])
        return action

    if position == 7:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 8:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = productCard(position, obj, business, lang, restp,'')
        da = []
        for i in message:
            action = sendProductMsg(phone, i)
            da.append(action)
        return da
    if position == 9:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = productCard(position, obj, business, lang, restp,txt)
        da = []
        for i in message:
            action = sendProductMsg(phone, i)
            da.append(action)
        return da
    if position == 10:
        if txt =='':
            obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
            message = textMessage(position, '', obj, lang)
            action = sendTextMsg(phone, message)
            return action
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = productCard(position, obj, business, lang, restp,txt)
        da = []
        for i in message:
            action = sendProductMsg(phone, i)
            da.append(action)
        return da
    if position == 11:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = productCard(position, obj, business, lang, restp,txt)
        da = []
        for i in message:
            action = sendProductMsg(phone, i)
            da.append(action)
        return da
    if position == 13:
        conversation.step = 8
        conversation.save(update_fields=['step'])
        msg = cartProductAdd(conversation.extr, conversation)
        action = sendProductMsg(phone, msg)
        return action
    if position == 14:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = ''
        btn = interactionCreation(position, obj, business, lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 15:
        conversation.step = 8
        conversation.save(update_fields=['step'])
        msg = cartProductRemove(conversation.extr, conversation)
        action = sendProductMsg(phone, msg)
        return action
    if position == 16:

        message = cartSubTotal(conversation.extr, conversation, txt)

        action = sendProductMsg(phone, message)
        return action
    if position == 17:
        conversation.step = 16
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 18:
        trc = cartConfirm(conversation.extr, conversation)
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        ordr = confirmOrderDetail(conversation.extr, conversation)
        notif = sendTextMsg(phone, ordr[0])
        sendLoc = sendLocationMsg(phone, ordr[1], ordr[2], ordr[3], ordr[4])
        message = textMessage(position, trc, obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 19:
        cartCanceld(conversation.extr, conversation)
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 21:
        conversation.step = 22
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 22:
        obj_name.address = txt
        obj_name.save(update_fields=['address'])
        conversation.step = 23
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 23:
        obj_name.area = txt
        obj_name.save(update_fields=['area'])
        conversation.step = 18
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 26:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = listCreation(position, obj, business, lang)
        action = sendListMsg(phone, message[0], message[1], message[2], message[3])
        return action

    if position == 27:
        conversation.step = 26
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = faqTextMessage(position, mroe, obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 28:
        conversation.step = 4
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        rquest = LiveTextMessage(29, obj_name, obj, lang)
        rqs_msg = sendTextMsg(business.support, rquest)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action

# Service
def interServiceAction(phone, btn, business):
    obj_name = CustomerProfile.objects.get(phone=phone)
    conv = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    rply = WhatsMsgReply.objects.get(id=btn)
    if conv.step == 50:
        chk_nam = checkCustomer(phone)
        if chk_nam:
            lg = 1
            if rply.serial != "1":
                lg = business.lang
            conv.step = 53
            conv.lang = lg
            conv.save(update_fields=['lang', 'step'])
            return True
        lg = 1
        if rply.serial != "1":
            lg = business.lang
        conv.lang = lg
        conv.step = 52
        conv.save(update_fields=['lang', 'step'])
        return True

    if rply.step == 53:
        row = WhatsTempMsg.objects.get(id=rply.serial)
        conv.step = row.next
        conv.save(update_fields=['step'])
        return False
    if rply.step == 54:
        conv.step = 55
        conv.flt = rply.serial
        conv.save(update_fields=['step', 'flt'])
        return False

    if rply.step == 55:
        conv.step = 56
        conv.extr = rply.serial
        conv.save(update_fields=['step','extr'])
        return False
    # if rply.step == 56:
    #     conv.step = 57
    #     conv.extr = rply.serial
    #     conv.save(update_fields=['step'])
    #     return False
def serviceMaping(phone, business, txt):
    obj_name = CustomerProfile.objects.get(phone=phone)
    conversation = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    position = conversation.step
    lang = conversation.lang
    restp = conversation.flt
    mroe = conversation.extr

    if position == 50:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, business.name, obj, lang)
        btn = interactionCreation(position, obj,business, '')
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 51:
        conversation.step = 52
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=2)
        message = textMessage(52, business.name, obj, business.lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 52:

        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=53)
        message = textMessage(53, '', obj, lang)
        btn = interactionCreation(53, obj, '', lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 53:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        btn = interactionCreation(position, obj, '', lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 54:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        btn = interactionCreation(position, obj, business, lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 55:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = srviceCreation(position, obj, business, lang, restp)
        da = []
        for i in message:
            action = sendListMsg(phone, i['txt1'], i['txt2'], i['txt3'], i['lst'])
            da.append(action)
        return(da)
    # if position == 56:
    #     obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
    #     message=serviceCart(position, restp, obj, lang)
    #     action = sendListMsg(phone, message[0], message[1],message[2],message[3])
    #     return action
    if position == 56:
        message=addBooking(position, mroe, conversation, lang, obj_name)
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        crtBu = createBusAddress(position, obj, business,obj_name)
        action = sendTextMsg(phone, message)
        if action:
            notif = sendTextMsg(phone, crtBu[0])
            if notif:
                sendLoc =sendLocationMsg(phone, crtBu[1], crtBu[2], crtBu[3], crtBu[4])
                if sendLoc:
                    notf = sendTextMsg(business.support, crtBu[5])
        return action
    if position == 58:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        crtBu = getBusAddress(position, obj, business)
        notif = sendTextMsg(phone, crtBu[0])
        if notif:
            sendLoc = sendLocationMsg(phone, crtBu[1], crtBu[2], crtBu[3], crtBu[4])
        return sendLoc
    if position == 59:
        trc = cartCanceld(conversation.extr, conversation)
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action

    if position == 60:
        conversation.step = 53
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        rquest = LiveTextMessage(60, obj_name, obj, lang)
        rqs_msg = sendTextMsg(business.support, rquest)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action

# Simple
def interSimpleAction(phone, btn, business):
    obj_name = CustomerProfile.objects.get(phone=phone)
    conv = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    rply = WhatsMsgReply.objects.get(id=btn)
    if conv.step == 1:
        row = WhatsTempMsg.objects.get(id=rply.serial)
        step = 0
        chk_nam = checkCustomer(phone)
        if chk_nam:
            step = 80
        lg = 1
        if row.lg:
            lg = 2
        conv.lang = lg
        conv.step = step
        conv.save(update_fields=['lang', 'step'])
        return True
    if conv.step == 80:
        row = WhatsTempMsg.objects.get(id=rply.serial)
        conv.step = row.next
        conv.save(update_fields=['step'])
        return False
def simpleMaping(phone, business, txt):
    obj_name = CustomerProfile.objects.get(phone=phone)
    conversation = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    position = conversation.step
    lang = conversation.lang
    if position == 0:
        conversation.step = 2
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=2)
        message = textMessage(2, business.name, obj, '')
        action = sendTextMsg(phone, message)
        return action
    if position == 1:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, business.name, obj, '')
        btn = interactionCreation(position, obj, '', '')
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 2:
        next = 80
        obj_name.name = txt
        obj_name.save()
        conversation.step = next
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=next)
        message = textMessage(next, '', obj, lang)
        btn = interactionCreation(next, obj, '', lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 80:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, '', obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 81:
        message = addSimpleReq(position, txt, conversation, business, obj_name, lang)

        notif = sendTextMsg(phone, message[0])
        if notif:
            action = sendTextMsg(phone, message[1])
        return action

# Clinic

def clinicAction(phone, btn, business):
    obj_name = CustomerProfile.objects.get(phone=phone)
    conv = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    rply = WhatsMsgReply.objects.get(id=btn)
    if conv.step == 80:
        chk_nam = checkCustomer(phone)
        if chk_nam:
            lg = 1
            if rply.serial != "1":
                lg = business.lang
            conv.lang = lg
            conv.step = 83
            conv.save(update_fields=['lang', 'step'])
            return True
        lg = 1
        if rply.serial != "1":
            lg = business.lang
        conv.lang = lg
        conv.step = 82
        conv.save(update_fields=['lang', 'step'])
        return True
    if rply.step == 83:
        row = WhatsTempMsg.objects.get(id=rply.serial)
        conv.step = row.next
        conv.save(update_fields=['step'])
        return False
    if rply.step == 84:
        conv.extr = rply.serial
        conv.step = 85
        conv.save(update_fields=['step','extr'])
        return False
    if rply.step == 85:
        conv.extr = rply.serial
        conv.step = 86
        conv.save(update_fields=['step','extr'])
        return False
    if rply.step == 86:
        conv.extr = rply.serial
        conv.step = 87
        conv.save(update_fields=['step','extr'])
        return False

def clinicMaping(phone, business, txt):
    obj_name = CustomerProfile.objects.get(phone=phone)
    conversation = WhatsMsg.objects.get(name=obj_name, business=business, status='CREATED')
    position = conversation.step
    lang = conversation.lang
    extr = conversation.extr
    if position == 80:

        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, business.name, obj, lang)
        btn = interactionCreation(position, obj, business, lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 81:
        conversation.step = 82
        conversation.save(update_fields=['step'])
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, business.name, obj, business.lang)
        action = sendTextMsg(phone, message)
        message2 = textMessage(82, business.name, obj, lang)
        action2 = sendTextMsg(phone, message2)
        return action
    if position == 82:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, business.name, obj, lang)
        action = sendTextMsg(phone, message)
        return action
    if position == 83:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = textMessage(position, obj_name.name, obj, lang)
        btn = interactionCreation(position, obj, business, lang)
        action = sendInteractivMsg(phone, message, btn)
        return action
    if position == 84:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = clincListCreation(position, obj, business, lang,'')
        action = sendListMsg(phone, message[0], message[1], message[2], message[3])
        return action
    if position == 85:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = clincListCreation(position, obj, business, lang,extr)
        action = sendListMsg(phone, message[0], message[1], message[2], message[3])
        return action
    if position == 86:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        message = clincListCreation(position, obj, business, lang,extr)
        action = sendListMsg(phone, message[0], message[1], message[2], message[3])
        return action
    if position == 87:
        message = clinicBooking(position,business,conversation,lang,obj_name,extr)
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        crtBu = createBusAddress(position, obj, business, obj_name)
        action = sendTextMsg(phone, message)
        if action:
            notif = sendTextMsg(phone, crtBu[0])
            if notif:
                sendLoc = sendLocationMsg(phone, crtBu[1], crtBu[2], crtBu[3], crtBu[4])
                if sendLoc:
                    notf = sendTextMsg(business.support, crtBu[5])
        conversation.status='CONFIRMED'
        conversation.save(update_fields=['status'])
        return action

    if position == 88:
        obj = WhatsMsgConve.objects.create(con_name=conversation, msg=txt, step=position)
        crtBu = getBusAddress(position, obj, business)
        notif = sendTextMsg(phone, crtBu[0])
        if notif:
            sendLoc = sendLocationMsg(phone, crtBu[1], crtBu[2], crtBu[3], crtBu[4])
            return sendLoc