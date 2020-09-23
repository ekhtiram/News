from django.contrib import admin

# Register your models here.
from .models import gridapp, baslik, altbaslik, ekleyen
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import AdminSite

#son eylemleri silmek icin
#from django.contrib.admin.models import LogEntry
#LogEntry.objects.all().delete()

def etkin_yapma(modeladmin, news, queryset):
    queryset.update(is_active=False)
etkin_yapma.short_description = u"Seçili kullanıcılar nesnelerini etkin olmaktan kaldır"
class EtkinYapma(UserAdmin):
    actions = [etkin_yapma]

admin.site.unregister(User)
admin.site.register(User, EtkinYapma)

#gorev durumunu aktif veya deaktif etmek icin. ama kod calismiyor, arastirilip gelistirilmeli
#def all_tasks(modeladmin, request, queryset):
#    for qs in queryset:
#        print (qs.Ad)
#
#def complete_tasks(modeladmin, request, queryset):
#    queryset.update(Açıklama=True)
#complete_tasks.short_description = "Mark as complete"
#
#def incomplete_tasks(modeladmin, request, queryset):
#    queryset.update(Açıklama=False)
#complete_tasks.short_description = "Mark as not complete"

class baslikAdmin(admin.ModelAdmin):
    list_display = ("ad",)

class altbaslikAdmin(admin.ModelAdmin):
    list_display = ("ad",)

class ekleyenAdmin(admin.ModelAdmin):
    list_display = ("ad",)

class gridappAdmin(admin.ModelAdmin):
	list_display = ("Baslik","Alt_baslik","Ekleyen","Icerik","Resim","Oluşturulma_Tarihi")

	#sayfadaki kayit adeti, otomatik sayfalama yapacak
	list_per_page = 15
	exclude = ("Oluşturulma_Tarihi",)
	# Filtre ( süzgeç ) yapabilmemiz için hazır sorgu alanı
	list_filter = ("Oluşturulma_Tarihi",)
	# Arama yapabilmemiz için otomatik bir metin alanı oluşturur. Arayacağımız kelimeler Ad'a girdiğimiz kayıtlarda sorgulayacak.
	search_fields = ("Baslik",)
	# Kayıtları yıl, ay ve gün olarak otomatik filtreleme yaptırmak için gird üstünde listeleme yapar
	date_hierarchy  = "Oluşturulma_Tarihi"

class Meta:
	model = gridapp

admin.site.register(models.gridapp, gridappAdmin)
admin.site.register(models.baslik, baslikAdmin)
admin.site.register(models.altbaslik, altbaslikAdmin)
admin.site.register(models.ekleyen, ekleyenAdmin)
