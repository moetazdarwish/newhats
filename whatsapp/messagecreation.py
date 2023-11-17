from datetime import datetime, timedelta

from django.db.models import Q

from customers.models import *
from whatsapp.models import *

def secondLanguage(lang,obj):
    if lang == 2:
        text = obj.l_1
        return text
    if lang == 3:
        text = obj.l_2
        return text
    if lang == 4:
        text = obj.l_3
        return text
    if lang == 5:
        text = obj.l_4
        return text
    if lang == 6:
        text = obj.l_5
        return text


def textMessage(step, tmplt, obj, lang):
    lang = int(lang)
    mg = WhatsTempName.objects.get(step=step)
    lst = WhatsTempMsg.objects.filter(temp_name=mg, btn=False)
    message = ''
    for i in lst:
        if i.templt:
            msg = i.en
            if lang > 1:
                msg = secondLanguage(lang,i)
            txt = '{0} {1} \n'.format(msg, tmplt)
            WhatsMsgReply.objects.create(reply_to=obj,reptxt=txt, reply=txt, step=step)
            message += txt
        else:
            msg = i.en
            if lang > 1:
                msg = secondLanguage(lang,i)
            txt = '{0} \n'.format(msg)
            WhatsMsgReply.objects.create(reply_to=obj,reptxt=txt, reply=txt, step=step)
            message += txt
    return message
def interactionCreation(step, obj, business, lang):
    if step == 1 or step == 50 or step == 80:
        mg = WhatsTempName.objects.get(step=step)
        btn_lst = WhatsTempMsg.objects.filter(temp_name=mg, btn=True)
        btn = []
        rply = WhatsMsgReply.objects.create(reply_to=obj, serial='1', step=step)
        btn1 = {"type": "reply", "reply": {"id": rply.id, "title": btn_lst[0].en}}
        rply.reply = btn1
        rply.reptxt = btn_lst[0].en
        rply.save(update_fields=['reply','reptxt'])
        btn.append(btn1)
        lang = business.lang
        rply = WhatsMsgReply.objects.create(reply_to=obj, serial=lang, step=step)
        sdtxt = secondLanguage(lang,btn_lst[1])
        btn2 = {"type": "reply", "reply": {"id": rply.id, "title":sdtxt  }}
        rply.reply = btn2
        rply.reptxt = sdtxt
        rply.save(update_fields=['reply', 'reptxt'])
        btn.append(btn2)
        return btn
    if step == 3 or step == 4  or step == 7 or step == 23 or step == 53 or step == 83:
        mg = WhatsTempName.objects.get(step=step)
        btn_lst = WhatsTempMsg.objects.filter(temp_name=mg, btn=True)
        btn = []
        for bt in btn_lst:
            msg = bt.en
            if lang > 1:
                msg =  secondLanguage(lang,bt)
            rply = WhatsMsgReply.objects.create(reply_to=obj, serial=bt.id, step=step)
            txt = {"type": "reply", "reply": {"id": rply.id, "title": msg}}
            rply.reply = txt
            rply.reptxt = msg
            rply.save(update_fields=['reply', 'reptxt'])
            btn.append(txt)
        return btn
    if step == 5:
        cat = InvCategory.objects.filter(business=business)
        btn = []
        for bt in cat:
            msg = bt.cate
            if lang > 1:
                msg = bt.cat_lc
            rply = WhatsMsgReply.objects.create(reply_to=obj, serial=bt.id, step=step)
            txt = {"type": "reply", "reply": {"id": rply.id, "title": msg}}
            rply.reply = txt
            rply.reptxt = msg
            rply.save(update_fields=['reply', 'reptxt'])
            btn.append(txt)
        return btn
    if step == 14:
        mg = WhatsTempName.objects.get(step=step)
        btn_lst = WhatsTempMsg.objects.filter(temp_name=mg, btn=True)
        btn = []
        for bt in btn_lst:
            msg = bt.en
            if lang > 1:
                msg = secondLanguage(lang,bt)
            rply = WhatsMsgReply.objects.create(reply_to=obj, serial=bt.id, step=step)
            txt = {"type": "reply", "reply": {"id": rply.id, "title": msg}}
            rply.reply = txt
            rply.reptxt = msg
            rply.save(update_fields=['reply', 'reptxt'])
            btn.append(txt)
        return btn
    if step == 54:
        cat = AppCategory.objects.filter(business=business)
        btn = []

        for bt in cat:
            msg = bt.cate
            if lang > 1:
                msg = bt.cat_lc
            rply = WhatsMsgReply.objects.create(reply_to=obj, serial=bt.id, step=step,extr='cat')
            txt = {"type": "reply", "reply": {"id": rply.id, "title": msg}}
            rply.reply = txt
            rply.reptxt = msg
            rply.save(update_fields=['reply', 'reptxt'])
            btn.append(txt)
        return btn
def productCard(step, obj, business, lang, cat,filter):
    cat = InvCategory.objects.get(id=cat)
    prod = ''
    if step == 8:
        prod = Inventory.objects.filter(category=cat, business=business)
    if step == 9:
        prod = Inventory.objects.filter(category=cat, business=business,price__lte=filter)
    if step == 10:
        prod = Inventory.objects.filter(Q(product__icontains=filter)|Q(product_lc__icontains=filter),category=cat, business=business)
    if step == 11:
        prod = Inventory.objects.filter(category=cat, business=business,offer=True)
    lst = []
    for i in prod:
        if i.h_url:
            btn = WhatsMsgReply.objects.create(reply_to=obj, serial=i.id, extr='PROD', step=step)
            nam = i.product
            price = i.price
            unit = i.unit
            descrp = i.Description
            if lang > 1:
                nam = i.product_lc
                descrp = i.Description_lc

            dta = {
                    "type": "button",
                    "body": {
                        "text": '{0} \n {1} - {2} \n {3}'.format(nam, price, unit, descrp)
                    },
                    "action": {
                        "buttons": [{"type": "reply", "reply": {"id": btn.id, "title": "Add"}},
                                    {"name": "cta_url", "parameters": {
                                            "display_text": "Info",
                                            "url": i.url}}]
                    }
                }
        else:
            btn = WhatsMsgReply.objects.create(reply_to=obj, serial=i.id, extr='PROD', step=step)
            nam = i.product
            price = i.price
            unit = i.unit
            descrp = i.Description
            if lang > 1:
                nam = i.product_lc
                descrp = i.Description_lc
            dta = {
                "type": "button",
                "body": {
                    "text": '{0} \n {1} - {2} \n {3}'.format(nam, price, unit, descrp)
                },
                "action": {
                    "buttons": [{"type": "reply", "reply": {"id": btn.id, "title": "Add"}}]
                }
            }
        btn.reply = dta
        btn.reptxt = '{0}  {1} - {2}  {3}'.format(nam, price, unit, descrp)
        btn.save(update_fields=['reply', 'reptxt'])
        lst.append(dta)
    return lst


def filterListCreation(step, obj, business, lang):
    if step == 6:
        mg = WhatsTempName.objects.get(step=step)
        btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
        txt1 = btn_lst[0].en
        txt2 = btn_lst[1].en
        txt3 = btn_lst[2].en

        if lang > 1:
            txt1 = secondLanguage(lang, btn_lst[0])
            txt2 = secondLanguage(lang, btn_lst[1])
            txt3 = secondLanguage(lang, btn_lst[2])

        lst = []
        for i in btn_lst[3:]:
            msg = i.en
            if lang > 1:
                msg = secondLanguage(lang, i)
            rply = WhatsMsgReply.objects.create(reply_to=obj,reptxt=msg, serial=i.id, step=step)
            dta = {
                "id": rply.id,
                "title": msg,
                "description": ''
            }
            rply.reply = dta
            rply.save(update_fields=['reply'])
            lst.append(dta)

        return txt1, txt2, txt3, lst


def listCreation(step, obj, business, lang):
    if step == 26:
        mg = WhatsTempName.objects.get(step=step)
        btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
        txt1 = btn_lst[0].en
        txt2 = btn_lst[1].en
        txt3 = btn_lst[2].en
        if lang > 1:
            txt1 = secondLanguage(lang,btn_lst[0])
            txt2 = secondLanguage(lang,btn_lst[1])
            txt3 = secondLanguage(lang,btn_lst[2])
        faq_lst = FAQ.objects.filter(business=business)
        faq=[]
        for i in faq_lst:
            rply = WhatsMsgReply.objects.create(reply_to=obj, serial=i.id, step=step)
            qut = i.question
            if lang >1:
                qut = i.question_lc
            dta = {
                "id": i.id,
                "title": "",
                "description": qut
            }
            rply.reply = dta
            rply.reptxt = qut
            rply.save(update_fields=['reply', 'reptxt'])
            faq.append(dta)

        return txt1 ,txt2,txt3,faq


def faqTextMessage(step, faq, obj, lang):
    faq_ans = FAQ.objects.get(id=faq)
    message = ''
    msg = faq_ans.answer
    if lang > 1:
        msg = faq_ans.answer_lc
    txt = '{0} \n'.format(msg)
    WhatsMsgReply.objects.create(reply_to=obj,reptxt = msg, reply=txt, step=step)
    message += txt
    return message

def LiveTextMessage(step, cust, obj, lang):
    mg = WhatsTempName.objects.get(step=step)
    lst = WhatsTempMsg.objects.filter(temp_name=mg)
    message = ''
    tlt = lst[0].en
    name = lst[1].en + cust.name
    if lang >1 :
        tlt = secondLanguage(lang,lst[0])
        name = secondLanguage(lang,lst[1])  + cust.name
    txt = '{0} \n {1} \n {2}'.format(tlt,name,cust.phone)
    WhatsMsgReply.objects.create(reply_to=obj,reptxt = txt, reply=txt, step=step)
    message += txt
    return message

def srviceCreation(step, obj, business, lang,st):
    if step == 55:
        mg = WhatsTempName.objects.get(step=step)
        btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
        cat = AppCategory.objects.get(id=st)
        srce = Appointment.objects.filter(business=business,category=cat)
        price = btn_lst[0].en
        dates = btn_lst[1].en
        schd = btn_lst[2].en
        frm = btn_lst[3].en
        fto = btn_lst[4].en
        if lang > 1:
            price =  secondLanguage(lang,btn_lst[0])
            dates = secondLanguage(lang,btn_lst[1])
            schd = secondLanguage(lang,btn_lst[2])
            frm = secondLanguage(lang,btn_lst[3])
            fto = secondLanguage(lang,btn_lst[4])
        data=[]
        for i in srce:
            days = ServiceHoliday.objects.filter(appoiment=i,business=business)
            lst = []
            for x in days:

                rply = WhatsMsgReply.objects.create(reply_to=obj, serial=x.id, step=step)

                if x.off is False:
                    srv = i.service
                    dsc = i.Description
                    if lang > 1:
                        srv = secondLanguage(lang,i.service_cl)
                        dsc = secondLanguage(lang,i.Description_cl)
                    txt1 = '{0} \n {1} {2} \n {3}'.format(srv, price, i.price, dsc)
                    txt2 = dates
                    txt3 = schd
                    title = x.day
                    servic = '{0}: {1}  - {2}: {3} '.format(frm,x.start,fto,x.end)
                    if lang > 1:
                        title = x.day_cl
                    dta = {
                        "id": rply.id,
                        "title": title,
                        "description": servic}
                    rply.reply = dta
                    rply.reptxt = txt1
                    rply.save(update_fields=['reply','reptxt'])
                    lst.append(dta)

            dlt = {
                "txt1": txt1,
                "txt2": txt2,
                "txt3": txt3,
                "lst": lst,
            }
            WhatsMsgReply.objects.create(reply_to=obj, reply=dlt, step=step)
            data.append(dlt)
        return data

def createBusAddress(step, obj,buss,cust):
    message = ''
    txt = '{0} \n {1} \n {2} \n'.format(buss.name,buss.phone, buss.Address)
    WhatsMsgReply.objects.create(reply_to=obj, reply=txt, step=step)
    message += txt
    lat= buss.latitude
    long= buss.longitude
    name= buss.name
    address= buss.Address
    notif = 'New Booking Confirmed For {0} \n phone : {1}'.format(cust.name,cust.phone)
    return message ,lat , long , name ,address ,notif

def getBusAddress(step, obj,buss):
    message = ''
    txt = '{0} \n {1}\n {2} \n'.format(buss.name,buss.support, buss.Address)
    WhatsMsgReply.objects.create(reply_to=obj, reply=txt, step=step)
    message += txt
    lat= buss.latitude
    long= buss.longitude
    name= buss.name
    address= buss.Address

    return message ,lat , long , name ,address

def clincListCreation(step, obj, business, lang,extr):
    if step == 84:

        mg = WhatsTempName.objects.get(step=step)
        btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
        sub = ClincSub.objects.filter(business=business)
        text = btn_lst[0].en
        button = btn_lst[1].en
        title = btn_lst[0].en
        if lang > 1:
            text =  secondLanguage(lang,btn_lst[0])
            button =  secondLanguage(lang,btn_lst[1])
            title =  secondLanguage(lang,btn_lst[0])
        data=[]
        for i in sub:
            txtreply = i.name
            if lang > 1:
                txtreply = i.name_lc

            rply = WhatsMsgReply.objects.create(reply_to=obj,reptxt=txtreply, serial=i.id, step=step)
            dta = {
                "id": rply.id,
                "title": txtreply,
                "description": ''}

            rply.reply = dta
            rply.save(update_fields=['reply'])
            data.append(dta)
        return text, button, title, data
    if step == 85:
        mg = WhatsTempName.objects.get(step=step)
        btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
        sub = ClincSub.objects.get(id=extr)
        clic = ClincDays.objects.filter(business=business,sub=sub)
        text = btn_lst[0].en
        button = btn_lst[1].en
        title = btn_lst[0].en
        if lang > 1:
            text = secondLanguage(lang, btn_lst[0])
            button = secondLanguage(lang, btn_lst[1])
            title = secondLanguage(lang, btn_lst[0])
        data = []
        for i in clic:
            if not i.off :
                txtreply = i.day
                if lang > 1:
                    txtreply = i.day_cl
                rply = WhatsMsgReply.objects.create(reply_to=obj, reptxt=txtreply, serial=i.id, step=step)
                dta = {
                    "id": rply.id,
                    "title": txtreply,
                    "description": ''}

                rply.reply = dta
                rply.save(update_fields=['reply'])
                data.append(dta)
        return text,button,title,data
    if step == 86:
        mg = WhatsTempName.objects.get(step=step)
        btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
        clic = ClincDays.objects.get(id=extr)
        doc = ClincDoctor.objects.filter(business=business, days=clic)
        text = btn_lst[0].en
        button = btn_lst[1].en
        title = btn_lst[0].en
        price = btn_lst[2].en
        frm = btn_lst[3].en
        to = btn_lst[4].en
        if lang > 1:
            text = secondLanguage(lang, btn_lst[0])
            button = secondLanguage(lang, btn_lst[1])
            title = secondLanguage(lang, btn_lst[0])
            price = secondLanguage(lang, btn_lst[2])
            frm = secondLanguage(lang, btn_lst[3])
            to = secondLanguage(lang, btn_lst[4])
        data = []
        for i in doc:
            txtreply = i.name
            dscr = i.Description
            if lang > 1:
                txtreply = i.name_lc
                dscr = i.Description_cl
            rply = WhatsMsgReply.objects.create(reply_to=obj, reptxt=txtreply, serial=i.id, step=step)
            dis_txt = '{0} \n {1} {2} - {3} {4} \n {5} {6}'.format(dscr,frm,i.start,to,i.end,price,i.price)
            dta = {
                "id": rply.id,
                "title": txtreply,
                "description": dis_txt}

            rply.reply = dta
            rply.save(update_fields=['reply'])
            data.append(dta)
        return text, button, title, data
