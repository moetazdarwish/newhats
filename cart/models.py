from datetime import datetime
from decimal import Decimal
from random import randint

from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
from customers.models import CustomerProfile, BusinessUnit, Inventory, Appointment, ServiceHoliday, SlotBooking, \
    ClincDoctor
from whatsapp.models import WhatsMsg


class Cart(models.Model):
    cust = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True)
    conver = models.ForeignKey(WhatsMsg, on_delete=models.CASCADE, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    items = models.IntegerField(null=True, blank=True)
    note = models.TextField(null=True, blank=True, default='No Note')
    transaction_id = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=20, blank=True, null=True, default='CREATED')
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True,)

    def __str__(self):
        return f'{self.id} '

    class Meta:
        ordering = ['-create_date']

    @property
    def get_cart_total(self):
        orderitems = self.cartproducts_set.all()
        sub_total = sum([item.get_total for item in orderitems])
        return round(Decimal(sub_total), 2)
    @property
    def get_cart_items(self):
        orderitems = self.cartproducts_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

def create_random():
    range_start = 10 ** (5 - 1)
    range_end = (10 ** 5) - 1
    return randint(range_start, range_end)
def createTransaction_id(sender, instance, *args, **kwargs):
    if instance.transaction_id is None:
        timeTrans = str(datetime.now().timestamp())[:4]
        codeTrans = create_random()
        transaction_id = str(codeTrans) + timeTrans
        instance.transaction_id = transaction_id
    if instance.status == 'CONFIRM':
        instance.total = instance.get_cart_total
        instance.items = instance.get_cart_items
pre_save.connect(createTransaction_id, sender=Cart)


class CartProducts(models.Model):
    order = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    status = models.CharField(max_length=50, blank=True, null=True, default='CREATED')
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        ordering = ['-create_date']

    @property
    def get_total(self):
        total = self.price * self.quantity
        return total

def CartProductsJournal(sender, instance, *args, **kwargs):
    if instance.price is None:
        get_price = Inventory.objects.get(id=instance.product.id)
        instance.price = get_price.price
pre_save.connect(CartProductsJournal, sender=CartProducts)




class CartServiceLst(models.Model):
    cust = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True)
    conver = models.ForeignKey(WhatsMsg, on_delete=models.CASCADE, null=True)
    appoint= models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True)
    day= models.ForeignKey(ServiceHoliday, on_delete=models.CASCADE, null=True)
    slot= models.ForeignKey(SlotBooking, on_delete=models.CASCADE, null=True)
    slot_nm = models.IntegerField(default=1, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    transaction_id = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=50, blank=True, null=True, default='CREATED')
    date = models.DateField(null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        ordering = ['-create_date']

def CartServiceLstJournal(sender, instance, *args, **kwargs):
    if instance.price is None:
        get_price = Appointment.objects.get(id=instance.service.id)
        instance.price = get_price.price
    if instance.transaction_id is None:
        timeTrans = str(datetime.now().timestamp())[:4]
        codeTrans = create_random()
        transaction_id = str(codeTrans) + timeTrans
        instance.transaction_id = transaction_id
pre_save.connect(CartServiceLstJournal, sender=CartServiceLst)

class CartSimple(models.Model):
    cust = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True)
    conver = models.ForeignKey(WhatsMsg, on_delete=models.CASCADE, null=True)
    order = models.TextField(null=True,blank=True)
    transaction_id = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=50, blank=True, null=True, default='CREATED')
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

def CartSimpleJournal(sender, instance, *args, **kwargs):
    if instance.transaction_id is None:
        timeTrans = str(datetime.now().timestamp())[:4]
        codeTrans = create_random()
        transaction_id = str(codeTrans) + timeTrans
        instance.transaction_id = transaction_id
pre_save.connect(CartSimpleJournal, sender=CartSimple)

class ClinicCart(models.Model):
    cust = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True)
    conver = models.ForeignKey(WhatsMsg, on_delete=models.CASCADE, null=True)
    clinc = models.ForeignKey(ClincDoctor, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    transaction_id = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return f'{self.id} '
def ClinicCartJournal(sender, instance, *args, **kwargs):
    if instance.transaction_id is None:
        timeTrans = str(datetime.now().timestamp())[:4]
        codeTrans = create_random()
        transaction_id = str(codeTrans) + timeTrans
        instance.transaction_id = transaction_id
pre_save.connect(ClinicCartJournal, sender=ClinicCart)