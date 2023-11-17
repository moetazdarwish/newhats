import csv

from django.contrib.admin import ModelAdmin
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
# Create your views here.
from cart.models import Cart, CartProducts, CartServiceLst
from customers.models import BusinessCategory, BusinessUnit, AppCategory, Appointment, ServiceHoliday, SlotBooking, \
    InvCategory, Inventory, FAQ, CustomerProfile
from home.form import CreateUser

from whatsapp.models import WhatsMsg, WhatsMsgConve, WhatsMsgReply, WhatsTempName, WhatsTempMsg


def home(request):
    return render(request,'index.html')

def login(request):

    with open('watmsg5.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
        employees = WhatsTempMsg.objects.all()
        writer = csv.writer(csv_file)
        for employee in employees:
            # writer.writerow([employee.cat.id, employee.name, employee.step])
            writer.writerow([employee.temp_name.step, employee.en, employee.l_1,employee.next,employee.templt,employee.btn])
    return 'response'

    # if request.POST:
    #     username = request.POST.get('email')
    #     print(username)
    #     password = request.POST.get('pass')
    #     print(password)
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         get_user = User.objects.get(username=user)
    #         print('hello')
    #         return redirect (dash)
    #
    # return render(request,'login.html')
def logout_view(request):
    logout(request)
    return redirect('home')
def signup(request):
    if request.POST:
        Busname = request.POST.get('Busname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        sernum = request.POST.get('sernum')
        passwrd = request.POST.get('pass')
        suppnum = request.POST.get('suppnum')
        data = {
            'email': email,
            'username': email,
            'password1': passwrd,
            'password2': passwrd,
        }
        form = CreateUser(data)
        if form.is_valid():
            user = form.save()
            today = datetime.now().date()
            date = today + timedelta(days=7)
            BusinessUnit.objects.create(user=user,name=Busname,phone=sernum,support=suppnum,Address=address,stdate=today,
                                        endate=date,trial=True)
            return redirect(cart)
    return render(request,'signup.html')
def cart(request):
    if request.POST:
        plan = request.POST.get('plns')
        g_bs = BusinessUnit.objects.get(user=request.user)
        print(plan)
        g_bs.plan = plan
        g_bs.save(update_fields=['plan'])
        return render(request, 'confirm.html')
    # name = "planamount"
    return render(request, 'cart.html')


def whatsapp (request):
    g_bs = BusinessUnit.objects.get(user=request.user)
    context = {'token':g_bs.token, 'name': g_bs.name}
    return render(request, 'pages/setup/whatsapp.html', context)
def dash(request):
    g_bs = BusinessUnit.objects.get(user=request.user)
    print(g_bs.token)
    if g_bs.cat.id == 1:
        crt = Cart.objects.filter(business=g_bs)
        context = {'crt': crt,'bus':g_bs ,'srv':'prod','name':g_bs.name}
        return render(request,'dash.html',context)
    if g_bs.cat.id == 2:
        crt = CartServiceLst.objects.filter(business=g_bs)
        context = {'crt': crt,'bus':g_bs,'srv':'srv','name':g_bs.name }
        return render(request,'dash.html',context)
def dashsearch(request):
    g_bs = BusinessUnit.objects.get(user=request.user)
    srch=request.POST.get('serch')
    if g_bs.cat.id == 1:
        crt = Cart.objects.filter(business=g_bs,cust__phone__icontains=srch)
        context = {'crt': crt,'bus':g_bs ,'srv':'prod','name':g_bs.name}
        return render(request,'pages/dash/find.html',context)
    if g_bs.cat.id == 2:
        crt = CartServiceLst.objects.filter(business=g_bs,cust__phone__icontains=srch)
        context = {'crt': crt,'bus':g_bs,'srv':'srv','name':g_bs.name }
        return render(request,'pages/dash/find.html',context)

def orddetls(request,pk):
    g_bs = BusinessUnit.objects.get(user=request.user)
    crt = Cart.objects.get(id=pk)
    pcrt = CartProducts.objects.filter(order=crt)
    context = {'crt': crt,'bus':g_bs,'pcrt':pcrt,'name':g_bs.name }
    return render(request,'pages/dash/ordil.html',context)

def conv(request):
    g_bs = BusinessUnit.objects.get(user=request.user)
    crt = WhatsMsg.objects.filter(business=g_bs).order_by('-date')
    context = {'crt': crt, 'bus': g_bs,'name':g_bs.name}
    return render(request, 'pages/conver/conversation.html', context)
def allconvdtls(request,pk):
    g_bs = BusinessUnit.objects.get(user=request.user)
    wmsg = WhatsMsg.objects.get(id=pk)
    conv = WhatsMsgConve.objects.filter(con_name=wmsg)
    context = {'wmsg': wmsg,'bus':g_bs,'conv':conv,'name':g_bs.name }
    return render(request,'pages/dash/condetail.html',context)
def consearch(request):
    g_bs = BusinessUnit.objects.get(user=request.user)
    srch=request.POST.get('serch')
    crt = WhatsMsg.objects.filter(business=g_bs,name__phone__icontains=srch).order_by('-date')
    context = {'crt': crt,'bus':g_bs ,'name':g_bs.name}
    return render(request,'pages/conver/srch.html',context)
def convdtls(request,pk):
    g_bs = BusinessUnit.objects.get(user=request.user)
    if g_bs.cat.id == 1:
        crt = Cart.objects.get(id=pk)
        wmsg = WhatsMsg.objects.get(id=crt.conver.id)
        conv = WhatsMsgConve.objects.filter(con_name=wmsg)
        context = {'wmsg': wmsg,'bus':g_bs,'conv':conv,'name':g_bs.name }
        return render(request,'pages/dash/condetail.html',context)
    if g_bs.cat.id == 2:
        crt = CartServiceLst.objects.get(id=pk)
        wmsg = WhatsMsg.objects.get(id=crt.conver.id)
        conv = WhatsMsgConve.objects.filter(con_name=wmsg)
        context = {'wmsg': wmsg, 'bus': g_bs, 'conv': conv,'name':g_bs.name}
        return render(request, 'pages/dash/condetail.html', context)
def templ(request):
    g_bs = BusinessUnit.objects.get(user=request.user)
    temp = BusinessCategory.objects.all()
    gt = BusinessCategory.objects.get(id=1)
    nme = WhatsTempName.objects.filter(cat=gt)
    # lst = whatstempmsg.objects.filter(temp_name=nme)
    context = {'temp': temp, 'bus': g_bs,'lst':nme,'name':g_bs.name}
    return render(request, 'pages/templ/tempdetail.html', context)

def templSelection(request):
    temp = request.POST.get('temp')
    if temp == '1':
        context = {'sect': 'prod', }
        return render(request, 'pages/templ/prodct.html',context)
    if temp == '2':
        context = {'sect': 'serv', }
        return render(request, 'pages/templ/prodct.html',context)
def settPage(request):
    cat = BusinessCategory.objects.all()
    g_bs = BusinessUnit.objects.get(user=request.user)
    if g_bs.latitude:
        faq = False
        if g_bs.cat.id == 1:
            faq = True
        context = {'cat': cat,'crr':g_bs.cat.cat,'faq':faq,'name':g_bs.name}
        return render(request, 'setting1.html', context)
    context = { 'crr': g_bs.cat.cat,'name':g_bs.name}
    return render(request, 'pages/setup/setti.html', context)
def setting(request,pk):
    cat = BusinessCategory.objects.get(id=pk)
    if cat.id == 1:
        g_bs = BusinessUnit.objects.get(user=request.user)
        g_bs.cat = cat
        g_bs.save(update_fields=['cat'])
        return redirect(selectProdCat,pk=cat.id,action=None)
    if cat.id == 2:
        g_bs = BusinessUnit.objects.get(user=request.user)
        g_bs.cat = cat
        g_bs.save(update_fields=['cat'])
        bcat = AppCategory.objects.filter(business=g_bs)
        context = {'bcat': bcat,'name':g_bs.name}
        return render(request, 'servicesetting.html', context)

def selectProdCat(request,pk,action):
    if request.htmx :
        if action =='add':
            ename = request.POST.get('ename')
            lname = request.POST.get('lname')
            g_bs = BusinessUnit.objects.get(user=request.user)
            InvCategory.objects.create(business=g_bs,mcat=g_bs.cat,cate=ename,cat_lc=lname)
            bcat = InvCategory.objects.filter(business=g_bs,mcat=g_bs.cat)
            context = {'bcat': bcat,'cat':g_bs.id,'name':g_bs.name}
            return render(request, 'pages/product/sub_cat.html', context)
        if action =='del':
            g_bs = BusinessUnit.objects.get(user=request.user)
            InvCategory.objects.get(id=pk).delete()
            bcat = InvCategory.objects.filter(business=g_bs,mcat=g_bs.cat)
            context = {'bcat': bcat,'cat':g_bs.id,'name':g_bs.name}
            return render(request, 'pages/product/sub_cat.html', context)
    g_bs = BusinessUnit.objects.get(user=request.user)
    cat = BusinessCategory.objects.get(id=pk)
    bcat = InvCategory.objects.filter(business=g_bs,mcat=cat)
    context = {'bcat': bcat,'cat':cat.id,'name':g_bs.name}
    return render(request,'pages/product/sub_cat.html',context)
def selectCat(request,pk,action):
    if request.htmx :
        if action =='add':
            ename = request.POST.get('ename')
            lname = request.POST.get('lname')
            g_bs = BusinessUnit.objects.get(user=request.user)
            AppCategory.objects.create(business=g_bs,cate=ename,cat_lc=lname)
            bcat = AppCategory.objects.filter(business=g_bs)
            context = {'bcat': bcat,'name':g_bs.name}
            return render(request, 'servicesetting.html', context)
        if action =='del':
            g_bs = BusinessUnit.objects.get(user=request.user)
            AppCategory.objects.get(id=pk).delete()
            bcat = AppCategory.objects.filter(business=g_bs)
            context = {'bcat': bcat,'name':g_bs.name}
            return render(request, 'servicesetting.html', context)
    g_bs = BusinessUnit.objects.get(user=request.user)
    bcat = AppCategory.objects.filter(business=g_bs)
    context = {'bcat': bcat,'name':g_bs.name}
    return render(request,'servicesetting.html',context)

def productDetails(request,pk,action):
    if request.htmx:
        if action == 'add':
            cat = InvCategory.objects.get(id=pk)
            g_bs = BusinessUnit.objects.get(user=request.user)
            ename = request.POST.get('ename')
            lname = request.POST.get('lname')
            edes = request.POST.get('edes')
            ldes = request.POST.get('ldes')
            price = request.POST.get('price')
            unit = request.POST.get('unit')
            offer = request.POST.get('offer')
            photo = request.FILES['photo']
            Inventory.objects.create(product=ename,product_lc=lname,business=g_bs, category=cat,
                                          price=price,unit=unit,Description=edes,Description_lc=ldes,
                                          offer=offer,photo=photo)

            ap = Inventory.objects.filter(business=g_bs, category=cat)
            context = {'ap': ap, 'pk': cat.id}
            return render(request, 'pages/product/prodlst.html', context)
        if action == 'lst':
            ap = Inventory.objects.get(id=pk)
            context = {'ap': ap}
            return render(request, 'pages/product/detailproduct.html', context)
        if action == 'del':
            value = request.POST.get('data')

            Inventory.objects.get(id=value).delete()
            cat = InvCategory.objects.get(id=pk)
            g_bs = BusinessUnit.objects.get(user=request.user)
            ap = Inventory.objects.filter(business=g_bs, category=cat)
            context = {'ap': ap,'pk':pk}
            return render(request, 'pages/product/prodlst.html', context)
    cat = InvCategory.objects.get(id=pk)
    g_bs = BusinessUnit.objects.get(user=request.user)
    ap=Inventory.objects.filter(business=g_bs,category=cat)
    context = {'ap': ap,'pk':cat.id}
    return render(request, 'pages/product/productdetails.html',context)

def displayproduct(request,pk):
    ap = Inventory.objects.get(id=pk)
    context = {'ap': ap}
    return render(request, 'pages/product/detailproduct.html', context)
def serviceDetails(request,pk,action):
    if request.htmx:
        if action == 'add':
            cat = AppCategory.objects.get(id=pk)
            g_bs = BusinessUnit.objects.get(user=request.user)
            ap = Appointment.objects.create(business=g_bs, category=cat)
            ename = request.POST.get('ename')
            lname = request.POST.get('lname')
            edes = request.POST.get('edes')
            ldes = request.POST.get('ldes')
            price = request.POST.get('price')
            ap.service=ename
            ap.service_cl=lname
            ap.price=price
            ap.Description=edes
            ap.Description_cl=ldes
            ap.save()
            context = {'ap': ap.id,'name':g_bs.name}
            return render(request, 'servicesettingday.html', context)
        if action == 'lst':
            ap = Appointment.objects.get(id=pk)
            context = {'ap': ap.id}
            return render(request, 'servicesettingday.html', context)
        if action == 'del':
            value = request.POST.get('data')

            Appointment.objects.get(id=value).delete()
            cat = AppCategory.objects.get(id=pk)
            g_bs = BusinessUnit.objects.get(user=request.user)
            ap = Appointment.objects.filter(business=g_bs, category=cat)
            context = {'ap': ap,'pk':pk,'name':g_bs.name}
            return render(request, 'servicesettingdet.html', context)
    cat = AppCategory.objects.get(id=pk)
    g_bs = BusinessUnit.objects.get(user=request.user)
    ap=Appointment.objects.filter(business=g_bs,category=cat)
    context = {'ap': ap,'pk':pk,'name':g_bs.name}
    return render(request, 'servicesettingdet.html',context)

def addDaysService(request,pk,action):
    g_bs = BusinessUnit.objects.get(user=request.user)
    if request.htmx:
        if action == 'add':
            g_bs = BusinessUnit.objects.get(user=request.user)
            ap = Appointment.objects.get(id=pk)
            enday = request.POST.get('enday')
            daycl = request.POST.get('daycl')
            wrk = request.POST.get('wrk')
            if wrk == '2':
                try:
                    dy=ServiceHoliday.objects.get(appoiment=ap,business=g_bs, day_nm=enday )
                    dy.off = True
                    dy.save()
                    context = {'ap': pk,'name':g_bs.name}
                    return render(request, 'dylst.html', context)
                except:
                    ServiceHoliday.objects.create(appoiment=ap,business=g_bs, day_nm=enday,off=True ,day_cl = daycl)
                    context = {'ap': pk}
                    return render(request, 'dylst.html', context)
            time = request.POST.get('time')
            try:
                dy = ServiceHoliday.objects.get(appoiment=ap,business=g_bs, day_nm=enday)
                dy.off=False
                dy.save()
            except:
                dy = ServiceHoliday.objects.create(appoiment=ap,business=g_bs, day_nm=enday,off=False,day_cl = daycl)

            SlotBooking.objects.create(appoiment=ap,day=dy,start=time)
            sh = SlotBooking.objects.filter(appoiment=ap, day=dy)
            context = {'sh': sh, 'ap': pk}
            return render(request, 'dylst.html', context)
        if action == 'del':
            ap = Appointment.objects.get(id=pk)
            value = request.POST.get('value')
            print(value)
            dl = SlotBooking.objects.get(id=value)
            day = dl.day.day_nm
            dl.delete()
            try:
                print(day)
                dy = ServiceHoliday.objects.get(appoiment=ap, business=g_bs, day_nm=day)
                sh = SlotBooking.objects.filter(appoiment=ap, day=dy)
                context = {'sh': sh, 'ap': pk}
                return render(request, 'dylst.html', context)
            except:
                context = {'ap': pk}
                return render(request, 'dylst.html', context)
        if action == 'day':
            print(request.body)
            ap = Appointment.objects.get(id=pk)
            value = request.POST.get('wrk')
            day = request.POST.get('enday')
            try:
                dy = ServiceHoliday.objects.get(appoiment=ap, business=g_bs,day_nm=day)
                if value =='2':
                    dy.off = True
                    dy.save()
                    context = {'ap': pk}
                    return render(request, 'dylst.html', context)
                if value == '1':
                    dy.off = False
                    dy.save()
                    sh = SlotBooking.objects.filter(appoiment=ap, day=dy)
                    context = {'sh': sh, 'ap': pk}
                    return render(request, 'dylst.html', context)
            except:
                context = {'ap': pk}
                return render(request, 'dylst.html', context)
        if action == 'all':
            ap = Appointment.objects.get(id=pk)
            try:
                day = request.GET.get('enday')
                dy = ServiceHoliday.objects.get(appoiment=ap,business=g_bs, day_nm=day,off=False)
                sh = SlotBooking.objects.filter(appoiment=ap, day=dy)
                context = {'sh': sh, 'ap': pk}
                return render(request, 'dylst.html', context)
            except:
                context = {'ap': pk}
                return render(request, 'dylst.html', context)
    ap = Appointment.objects.get(id=pk)
    try:
        day = request.GET.get('enday')
        dy = ServiceHoliday.objects.get(appoiment=ap,business=g_bs,day_nm=day)
        sh = SlotBooking.objects.filter(appoiment=ap,day=dy)
        context = {'sh': sh, 'ap': pk}
        return render(request, 'dylst.html', context)
    except:

        context = { 'ap': pk}
        return render(request, 'dylst.html', context)

def prodFAQ(request,pk):
    if request.htmx :
        action = request.POST.get('action')
        if action =='add':
            equst = request.POST.get('equst')
            lqust = request.POST.get('lqust')
            ans = request.POST.get('ans')
            anslc = request.POST.get('anslc')
            g_bs = BusinessUnit.objects.get(user=request.user)
            cat = BusinessCategory.objects.get(id=pk)
            FAQ.objects.create(business=g_bs, cat=cat,question=equst,question_lc=lqust,answer=ans,answer_lc=anslc)
            faq = FAQ.objects.filter(business=g_bs, cat=cat)
            context = {'faq':faq,'pk':pk}
            return render(request, 'pages/product/faqlst.html', context)
        if action =='del':
            fadel = request.POST.get('fadel')
            g_bs = BusinessUnit.objects.get(user=request.user)
            cat = BusinessCategory.objects.get(id=pk)
            FAQ.objects.get(id=fadel).delete()
            faq = FAQ.objects.filter(business=g_bs, cat=cat)
            context = {'faq':faq,'pk':cat.id}
            return render(request, 'pages/product/faqlst.html', context)
    g_bs = BusinessUnit.objects.get(user=request.user)
    cat = BusinessCategory.objects.get(id=pk)
    faq = FAQ.objects.filter(business=g_bs, cat=cat)
    context = {'faq':faq,'pk':pk,'name':g_bs.name}
    return render(request, 'pages/product/productfaq.html', context)

