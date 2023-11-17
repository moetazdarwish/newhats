import uuid
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.

def Raw_Products_path(instance, filename):
    return 'inventory/{0}'.format(filename)

class BusinessCategory(models.Model):
    cat = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return '{0}-{1}'.format(self.id,self.cat)


class BusinessUnit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    ph_acc = models.CharField(max_length=30, null=True, blank=True)
    ph_tkn = models.CharField(max_length=300, null=True, blank=True)
    support = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    cat = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE, null=True, blank=True)
    stdate = models.DateField(null=True, blank=True)
    endate = models.DateField(null=True, blank=True)
    trial = models.BooleanField(default=False, null=True, blank=True)
    lang = models.IntegerField(default=1, null=True, blank=True)
    extlang = models.BooleanField(default=False, null=True, blank=True)
    plan = models.IntegerField(default=0, null=True, blank=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} '


class CustomerProfile(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    area = models.CharField(max_length=15, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.name} '


class InvCategory(models.Model):
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True, blank=True)
    mcat = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE, null=True, blank=True)
    cate = models.CharField(max_length=50, null=True, blank=True)
    cat_lc = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cate} '

class Inventory(models.Model):
    product = models.CharField(max_length=50, null=True, blank=True)
    product_lc = models.CharField(max_length=50, null=True, blank=True)
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(InvCategory, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    unit = models.CharField(max_length=10,null=True, blank=True)
    Description = models.CharField(max_length=150, null=True, blank=True)
    Description_lc = models.CharField(max_length=150, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    h_url = models.BooleanField(default=False, null=True, blank=True)
    photo = models.FileField(blank=True, null=True, default='prodct.png', upload_to=Raw_Products_path,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    offer = models.BooleanField(default=False,null=True,blank=True)
    date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} '


class InventoryImage(models.Model):
    inv = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.FileField(blank=True, null=True, default='prodct.png', upload_to=Raw_Products_path,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    def __str__(self):
        return f'{self.inv.product} '

class AppCategory(models.Model):
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True, blank=True)
    mcat = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE, null=True, blank=True)
    cate = models.CharField(max_length=50, null=True, blank=True)
    cat_lc = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cate} '
class Appointment(models.Model):
    service = models.CharField(max_length=50, null=True, blank=True)
    service_cl = models.CharField(max_length=50, null=True, blank=True)
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(AppCategory, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True,)
    Description = models.CharField(max_length=150, null=True, blank=True)
    Description_cl = models.CharField(max_length=150, null=True, blank=True)
    photo = models.FileField(blank=True, null=True, default='prodct.png', upload_to=Raw_Products_path,
                             validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    start = models.TimeField(null=True,blank=True)
    end = models.TimeField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service} '

class ServiceHoliday(models.Model):
    appoiment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True,blank=True)
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True, blank=True)
    day_nm = models.IntegerField(default=0,null=True,blank=True)
    day = models.CharField(max_length=20,null=True,blank=True)
    day_cl = models.CharField(max_length=20,null=True,blank=True)
    off = models.BooleanField(default=False,null=True,blank=True)
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{0} - {1} '.format(self.day,self.appoiment)

class SlotBooking(models.Model):
    appoiment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True,blank=True)
    day = models.ForeignKey(ServiceHoliday, on_delete=models.CASCADE, null=True, blank=True)
    slot_nm = models.IntegerField(default=1,null=True,blank=True)
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.appoiment.service} '

class FAQ(models.Model):
    business = models.ForeignKey(BusinessUnit,on_delete=models.CASCADE,null=True,blank=True)
    cat = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=100, null=True, blank=True)
    question_lc = models.CharField(max_length=100, null=True, blank=True)
    answer = models.CharField(max_length=200, null=True, blank=True)
    answer_lc = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class ClincSub(models.Model):
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    name_lc = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} '
class ClincDays(models.Model):
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True, blank=True)
    sub = models.ForeignKey(ClincSub, on_delete=models.CASCADE, null=True, blank=True)
    day_nm = models.IntegerField(default=0, null=True, blank=True)
    day = models.CharField(max_length=20, null=True, blank=True)
    day_cl = models.CharField(max_length=20, null=True, blank=True)
    off = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.day} '

class ClincDoctor(models.Model):
    business = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True, blank=True)
    days = models.ForeignKey(ClincDays, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    name_lc = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=150, null=True, blank=True)
    Description_cl = models.CharField(max_length=150, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} '
