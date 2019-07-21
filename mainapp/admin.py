from django.contrib import admin
from .models import Proje, Atolye, Burs, Contact, GonulluBasvuru, BursBasvuru
from django.contrib.auth.models import User, Group


class ProjeAdmin(admin.ModelAdmin):
    exclude = ('proje_slug',)
admin.site.register(Proje, ProjeAdmin)

class AtolyeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Atolye, AtolyeAdmin)

class BursAdmin(admin.ModelAdmin):
    exclude = ('burs_slug',)
admin.site.register(Burs, BursAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)

class GonulluBasvuruAdmin(admin.ModelAdmin):
    pass
admin.site.register(GonulluBasvuru, GonulluBasvuruAdmin)

class BursBasvuruAdmin(admin.ModelAdmin):
    pass
admin.site.register(BursBasvuru, BursBasvuruAdmin)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = 'Başak Sanat Yönetim Paneli'
