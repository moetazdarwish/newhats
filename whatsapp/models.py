from django.db import models

# Create your models here.
from customers.models import CustomerProfile, BusinessUnit, BusinessCategory


class WhatsMsg(models.Model):
    name = models.ForeignKey(CustomerProfile,on_delete=models.CASCADE,null=True,blank=True)
    business = models.ForeignKey(BusinessUnit,on_delete=models.CASCADE,null=True,blank=True)
    step = models.IntegerField(null=True,blank=True,default=1)
    extr = models.CharField(max_length=20,null=True,blank=True)
    lang = models.IntegerField(default=1,null=True,blank=True)
    flt = models.IntegerField( null=True, blank=True)
    status = models.CharField(max_length=50,null=True,blank=True,default='CREATED')
    date = models.DateTimeField(auto_now_add=True)

class WhatsMsgConve(models.Model):
    con_name = models.ForeignKey(WhatsMsg, on_delete=models.CASCADE, null=True, blank=True)
    msg = models.CharField(max_length=100,null=True, blank=True)
    reptxt = models.CharField(max_length=100, null=True, blank=True)
    step = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class WhatsMsgReply(models.Model):
    reply_to = models.ForeignKey(WhatsMsgConve, on_delete=models.CASCADE, null=True, blank=True)
    reptxt = models.CharField(max_length=100,null=True,blank=True)
    reply = models.CharField(max_length=120,null=True,blank=True)
    serial = models.CharField(max_length=10,null=True,blank=True)
    extr = models.CharField(max_length=20,null=True,blank=True)
    step = models.IntegerField(null=True, blank=True)
    flt = models.IntegerField(default=0,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class WhatsTempName(models.Model):
    cat = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    step = models.IntegerField(null=True, blank=True)
    lang = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{0} - {1} '.format(self.name, self.step)

    class Meta:
        ordering = ['-step']

class WhatsTempMsg(models.Model):
    temp_name = models.ForeignKey(WhatsTempName, on_delete=models.CASCADE, null=True, blank=True)
    en = models.CharField(max_length=100,null=True,blank=True)
    l_1 = models.CharField(max_length=100, null=True, blank=True)
    next = models.IntegerField(default=0, null=True, blank=True)
    templt = models.BooleanField(default=False,null=True,blank=True)
    btn = models.BooleanField(default=False,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    l_2 = models.CharField(max_length=100, null=True, blank=True)
    l_3 = models.CharField(max_length=100, null=True, blank=True)
    l_4 = models.CharField(max_length=100, null=True, blank=True)
    l_5 = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f'{self.temp_name.name} '

