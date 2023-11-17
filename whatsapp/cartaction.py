from datetime import datetime, timedelta

from cart.models import Cart, CartProducts, CartServiceLst, CartSimple, ClinicCart
from customers.models import Inventory, ServiceHoliday, SlotBooking, ClincDoctor
from whatsapp.messagecreation import secondLanguage
from whatsapp.models import WhatsMsgConve, WhatsTempName, WhatsTempMsg, WhatsMsgReply


def cartProductAdd(prod,conv):
    get_prod = Inventory.objects.get(id=prod)
    crt , create = Cart.objects.get_or_create(cust=conv.name,business=conv.business,conver=conv,status='CREATED')
    sub , create = CartProducts.objects.get_or_create(order=crt,product=get_prod)
    sub.quantity = sub.quantity + 1
    sub.save()
    txt = 'add - {0}'.format(get_prod.product)
    obj = WhatsMsgConve.objects.create(con_name=conv, msg=txt, step=8)
    mg = WhatsTempName.objects.get(step=13)
    lst = WhatsTempMsg.objects.filter(temp_name=mg)

    title = lst[0].en
    prduct = get_prod.product
    qty = sub.quantity
    fot = lst[1].en
    btn1 = lst[2].en
    btn2 = lst[3].en
    if conv.lang > 1:
        title = secondLanguage(conv.lang,lst[0])
        fot = secondLanguage(conv.lang,lst[1])
        btn1 = secondLanguage(conv.lang,lst[2])
        btn2 = secondLanguage(conv.lang,lst[3])
        prduct = get_prod.product_lc
    btn1_rep = WhatsMsgReply.objects.create(reply_to=obj, serial=lst[2].id, extr='DET', step=15)
    btn2_rep = WhatsMsgReply.objects.create(reply_to=obj, serial=lst[3].id, extr='ACT', step=14)
    dta ={

            "type": "button",
            "body": {
                "text": '{0} \n {1} \n {2} \n'.format(title,prduct,qty,fot)
            },
            "action": {
                "buttons": [
                    {"type": "reply", "reply": {"id": btn1_rep.id, "title": btn1}},
                    {"type": "reply", "reply": {"id": btn2_rep.id, "title": btn2}}
                ]
            }
        }
    btn1_rep.reply = dta
    btn1_rep.reptxt = btn1
    btn1_rep.save(update_fields=['reply', 'reptxt'])
    btn2_rep.reply = dta
    btn2_rep.reptxt = btn2
    btn2_rep.save(update_fields=['reply', 'reptxt'])

    return dta


def cartProductRemove(row,conv):
    sub = CartProducts.objects.get(id=row)
    sub.quantity = sub.quantity - 1
    sub.save()
    txt = 'removed - {0}'.format(sub.product.product)
    obj = WhatsMsgConve.objects.create(con_name=conv, msg=txt, step=14)
    mg = WhatsTempName.objects.get(step=14)
    lst = WhatsTempMsg.objects.filter(temp_name=mg)
    title = lst[0].en
    prduct = sub.product.product
    qty = sub.quantity
    fot = lst[1].en
    btn1 = lst[2].en
    if conv.lang >1:
        title = secondLanguage(conv.lang,lst[0])
        fot = secondLanguage(conv.lang,lst[1])
        btn1 = secondLanguage(conv.lang,lst[2])
        prduct = sub.product.product_lc
    btn1_rep = WhatsMsgReply.objects.create(reply_to=obj, serial=sub.order.id, extr='ACT', step=13)
    dta ={
            "type": "button",
            "body": {
                "text": '{0} \n {1} \n {2} \n'.format(title,prduct,qty,fot)
            },
            "action": {
                "buttons": [
                    {"type": "reply", "reply": {"id": btn1_rep.id, "title": btn1}},

                ]
            }
        }
    if sub.quantity == 0:
        sub.delete()
    btn1_rep.reply = dta
    btn1_rep.reptxt = btn1
    btn1_rep.save(update_fields=['reply', 'reptxt'])
    return dta

def cartSubTotal(cart_id, conv,txt):
    lang=conv.lang
    crt = Cart.objects.get(id=cart_id)
    crt.note = txt
    crt.save(update_fields=['note'])
    sub = CartProducts.objects.filter(order=crt)

    obj = WhatsMsgConve.objects.create(con_name=conv, msg=txt, step=16)
    mg = WhatsTempName.objects.get(step=16)
    lst = WhatsTempMsg.objects.filter(temp_name=mg)
    message = ''
    title = lst[0].en
    if lang > 1:
        title = secondLanguage(conv.lang,lst[0])
    txt = '{0} \n'.format(title)
    message +=txt
    for i in sub:
        product = i.product.product
        if lang >1:
            product = i.product.product_lc
        msg = '{0} - {1}  {2} \n'.format(product,i.quantity,i.get_total)
        message += msg

    total = lst[1].en
    if lang > 1:
        total = secondLanguage(conv.lang,lst[1])
    tot = '{0} \n'.format(total)
    message += tot
    btn1 = lst[2].en
    btn2 = lst[3].en
    if conv.lang > 1:
        btn1 = secondLanguage(conv.lang,lst[2])
        btn2 = secondLanguage(conv.lang,lst[3])
    btn1_rep = WhatsMsgReply.objects.create(reply_to=obj, serial=lst[2].id, extr='DET', step=16)
    btn2_rep = WhatsMsgReply.objects.create(reply_to=obj, serial=lst[3].id, extr='CRF', step=16)
    dta = {
        "type": "button",
        "body": {
            "text": message
        },
        "action": {
            "buttons": [
                {"type": "reply", "reply": {"id": btn1_rep.id, "title": btn1}},
                {"type": "reply", "reply": {"id": btn2_rep.id, "title": btn2}}
            ]
        }
    }
    btn1_rep.reply = dta
    btn1_rep.reptxt = btn1
    btn1_rep.save(update_fields=['reply', 'reptxt'])
    btn2_rep.reply = dta
    btn2_rep.reptxt = btn2
    btn2_rep.save(update_fields=['reply', 'reptxt'])
    return dta

def cartConfirm(cart_id, conv):
    crt= Cart.objects.get(id=cart_id)
    crt.status='CONFIRM'
    crt.save()
    conv.status='CONFIRM'
    conv.save()

    return crt.transaction_id

def cartCanceld(cart_id, conv):
    crt= Cart.objects.get(id=cart_id)
    crt.status='CANCEL'
    crt.save()
    conv.status='CANCEL'
    conv.save()
    return 'done'

def confirmOrderDetail(cart_id, conv):
    lang=conv.lang
    crt = Cart.objects.get(id=cart_id)
    sub = CartProducts.objects.filter(order=crt)
    obj = WhatsMsgConve.objects.create(con_name=conv, msg='CONF', step=18)
    mg = WhatsTempName.objects.get(step=18)
    lst = WhatsTempMsg.objects.filter(temp_name=mg)
    long =crt.cust.longitude
    lat = crt.cust.latitude
    message = ''
    No = crt.transaction_id
    name = crt.cust.name
    phone = crt.cust.phone
    address = crt.cust.address
    area = crt.cust.area
    note = crt.note
    txt = '{0} \n {1} \n {2} \n {3} - {4} \n  {5} \n Order \n '.format(No,name,phone,address,area,note)
    message +=txt
    for i in sub:
        product = i.product.product
        if lang > 1:
            product = i.product.product_lc
        msg = '{0} - {1}  {2} \n'.format(product,i.quantity,i.get_total)
        message += msg

    total = lst[1].en
    if lang > 1:
        total = secondLanguage(lang,lst[1])
    tot = '{0} \n'.format(total)
    message += tot


    WhatsMsgReply.objects.create(reply_to=obj,reptxt=msg,reply=message, extr='CONF', step=18)

    return message ,lat , long , name ,address

def gtdate(n):
    dt = datetime.now().weekday()
    today = datetime.now().date()
    if dt > n:
        fd= 7-dt
        sd=0
        for i in range(0-dt):
            sd+=1
        bd=fd+sd
        date = today + timedelta(days=bd)
        return date
    if n > dt:
        fd = n-dt
        date = today + timedelta(days=fd)
        return date
    else :
        date = today
        return date

def serviceCart(step,srv,obj,lang):
    mg = WhatsTempName.objects.get(step=step)
    btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
    days = ServiceHoliday.objects.get(id=srv)
    date = gtdate(days.day_nm)
    get_slot = SlotBooking.objects.filter(day=days)
    slt=[]
    txt1 = btn_lst[0].en
    txt2 = btn_lst[1].en
    txt3 = btn_lst[2].en
    if lang > 1:
        txt1 =secondLanguage(lang,btn_lst[0])
        txt2 = secondLanguage(lang,btn_lst[1])
        txt3 = secondLanguage(lang,btn_lst[2])
    for i in get_slot:
        if CartServiceLst.objects.filter(day=days, date=date,slot=i,slot_nm=i.slot_nm):
            pass
        else:
            rply = WhatsMsgReply.objects.create(reply_to=obj, serial=i.id, step=step)
            tim = str(datetime.strptime(str(i.start),'%H:%M:%S').time())
            dta = {
                "id": rply.id,
                "title": tim,
                "description": ""}
            rply.reply = dta
            rply.reptxt = tim
            rply.save(update_fields=['reply', 'reptxt'])
            slt.append(dta)
    return txt1,txt2,txt3,slt

def addBooking(step,srv,obj,lang,cust):
    get_slot = ServiceHoliday.objects.get(id=srv)

    mg = WhatsTempName.objects.get(step=step)
    btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)

    date = gtdate(get_slot.day_nm)
    CartServiceLst.objects.create(cust=cust,business=get_slot.business,conver=obj
                                  ,appoint=get_slot.appoiment
                                  ,day=get_slot,
                                  date=date,status='CONFIRMED')
    message = ''
    txt1 = btn_lst[0].en
    if lang > 1:
        txt1 = secondLanguage(lang,btn_lst[0])
    obj.status='CONFIRMED'
    obj.save()
    objrp = WhatsMsgConve.objects.create(con_name=obj, msg='CONFIRMED', step=53)
    rply = WhatsMsgReply.objects.create(reply_to=objrp,reptxt=txt1,reply=txt1,step=step)
    message += '{0}'.format(txt1)

    return message

def cancelBooking(step,srv,obj,lang,cust):
    mg = WhatsTempName.objects.get(step=step)
    btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
    today = datetime.now().date()

    CartServiceLst.objects.get(cust=cust)
    message = ''
    txt1 = btn_lst[0].en
    if lang > 1:
        txt1 = secondLanguage(lang,btn_lst[0])
    message += '{0}'.format(txt1)
    rply = WhatsMsgReply.objects.create(reply_to=obj, reply=txt1, step=step)
    return message


def addSimpleReq(step,txt,obj,business,cust,lang):
    obj.status='CONFIRM'
    obj.save()
    CartSimple.objects.create(cust=cust,business=business,conver=obj,order=txt,status='CONFIRM')
    objrp = WhatsMsgConve.objects.create(con_name=obj, msg=txt, step=step)
    rply = WhatsMsgReply.objects.create(reply_to=objrp, reply=txt, step=step)
    mg = WhatsTempName.objects.get(step=81)
    btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
    message = ''
    txt1 = btn_lst[0].en
    if lang > 1:
        txt1 = secondLanguage(lang,btn_lst[0])
    message += '{0}'.format(txt1)
    noti = '{0} \n {1} \n {2}'.format(cust.name,cust.phone,txt)

    rply.reptxt = noti
    rply.save(update_fields=['reptxt'])
    return message , noti

def clinicBooking(step,business,obj,lang,cust,extr):
    get_doc = ClincDoctor.objects.get(id=extr)
    ClinicCart.objects.create(cust=cust,business=business,conver=obj,clinc=get_doc,price=get_doc.price)
    mg = WhatsTempName.objects.get(step=step)
    btn_lst = WhatsTempMsg.objects.filter(temp_name=mg)
    message = ''
    text = btn_lst[0].en
    doc = get_doc.name
    if lang > 1:
        text = secondLanguage(lang, btn_lst[0])
        doc = get_doc.name_lc

    message += text
    message += '\n {0} \n {1} \n {2}'.format(doc,get_doc.start,get_doc.price)
    obj = WhatsMsgConve.objects.create(con_name=obj, msg=doc, step=step)
    rply = WhatsMsgReply.objects.create(reply_to=obj, reptxt=message, reply=message, step=step)
    return message
