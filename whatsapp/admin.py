import csv

from django.contrib import admin

# Register your models here.
from django.http import HttpResponse

from whatsapp.models import *

admin.site.register(WhatsMsgReply)
admin.site.register(WhatsTempMsg)

class WhatsTempMsgInline(admin.TabularInline):
    model = WhatsTempMsg
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra
class WhatsTempNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'step','lang']
    inlines = [WhatsTempMsgInline]
admin.site.register(WhatsTempName, WhatsTempNameAdmin)


class WhatsMsgReplyInline(admin.TabularInline):
    model = WhatsMsgReply
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra
class WhatsMsgConveAdmin(admin.ModelAdmin):
    list_display = ['msg', 'step']
    inlines = [WhatsMsgReplyInline]
admin.site.register(WhatsMsgConve, WhatsMsgConveAdmin)

class WhatsMsgInline(admin.TabularInline):
    model = WhatsMsgConve

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra
class WhatsMsgAdmin(admin.ModelAdmin):
    list_display = ['name', 'step','extr','status']
    inlines = [WhatsMsgInline]
admin.site.register(WhatsMsg, WhatsMsgAdmin)



