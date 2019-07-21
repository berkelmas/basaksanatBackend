from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

from django.db.models.signals import post_delete
from django.dispatch import receiver

from unidecode import unidecode

# Create your models here.
class Proje(models.Model):
    proje_baslik = models.CharField(('Proje Adı'), max_length= 150)
    proje_yayintarihi = models.DateField(('Proje Tarihi'), auto_now_add= True)
    proje_icerik = RichTextField(('Proje İçeriği'))
    proje_resim = models.ImageField(('Proje Resmi 870x400'))

    proje_slug = models.SlugField(unique= True)

    class Meta:
        verbose_name= 'Proje'
        verbose_name_plural= 'Projeler'
        ordering= ('-proje_yayintarihi',)

    def __str__(self):
        return self.proje_baslik

    def save(self, *args, **kwargs):
        self.proje_slug = slugify(unidecode(self.proje_baslik))
        super(Proje, self).save(*args, **kwargs)

class Atolye(models.Model):
    atolye_baslik = models.CharField(('Atölye Adı'), max_length= 150)
    atolye_donem = models.CharField(('Atölye Dönemi'), max_length= 100)
    atolye_icerik = models.TextField(('Atölye Açıklaması'))

    atolye_eklemetarihi = models.DateField(auto_now_add= True)

    class Meta:
        verbose_name= 'Atölye'
        verbose_name_plural= 'Atölyeler'
        ordering = ('-atolye_eklemetarihi',)

    def __str__(self):
        return self.atolye_baslik

class Burs(models.Model):
    burs_baslik = models.CharField(('Burs Başlığı'), max_length= 150)
    burs_icerik = RichTextField(('Burs İçeriği'))
    burs_resim = models.ImageField(('Burs Resmi 870x400'))
    burs_aktiflik = models.BooleanField(('Burs Aktiflik Durumu'))

    burs_slug = models.SlugField(unique= True)
    burs_yayintarihi = models.DateField(auto_now_add= True)

    class Meta:
        verbose_name = 'Burs'
        verbose_name_plural= 'Burslar'
        ordering = ('-burs_yayintarihi',)

    def __str__(self):
        return self.burs_baslik

    def save(self, *args, **kwargs):
        self.burs_slug = slugify(unidecode(self.burs_baslik))
        super(Burs, self).save(*args, **kwargs)

class Contact(models.Model):
    contact_name = models.CharField(('İsim'), max_length= 150)
    contact_email = models.CharField(('Email Adresi'), max_length= 150)
    contact_mesaj = models.TextField(('İletişim Mesajı'))

    contact_tarih = models.DateField(('İletişim Talebi Tarihi'), auto_now_add= True)

    class Meta:
        verbose_name= 'İletişim Talebi'
        verbose_name_plural= 'İletişim Talepleri'
        ordering= ('-contact_tarih',)

    def __str__(self):
        return self.contact_name

class GonulluBasvuru(models.Model):
    gonullu_isim = models.CharField(('Gönüllü İsmi'), max_length= 100)
    gonullu_email = models.CharField(('Gönüllü Email Adresi'), max_length= 150)
    gonullu_telefon = models.CharField(('Gönüllü Telefon Numarası'), max_length= 100)
    gonullu_calismaalani = models.CharField(('Gönüllü Çalışma Alanı'), max_length= 100)
    gonullu_baslamatarihi = models.CharField(('Gönüllü Başlangıç Tarihi'), max_length= 100)
    gonullu_mesaj = models.TextField(('Gönüllü Mesajı'))

    gonullu_basvurutarihi = models.DateField(('Gönüllü Başvuru Tarihi'), auto_now_add= True)

    class Meta:
        verbose_name= 'Gönüllü Başvurusu'
        verbose_name_plural= 'Gönüllü Başvuruları'
        ordering = ('-gonullu_basvurutarihi',)

    def __str__(self):
        return self.gonullu_isim

class BursBasvuru(models.Model):
    bursbasvuru_isim = models.CharField(('İsim-Soyisim'), max_length= 150)
    bursbasvuru_email = models.CharField(('Başvuran Email'), max_length= 150)
    bursbasvuru_telefon = models.CharField(('Başvuran Telefon'), max_length= 150)
    bursbasvuru_basvurulanburs = models.CharField(('Başvurulan Burs'), max_length= 150)
    bursbasvuru_mesaj = models.TextField(('Başvuran Mesajı'))

    bursbasvuru_tarih = models.DateField(('Başvuru Tarihi'), auto_now_add= True)

    class Meta:
        verbose_name = 'Burs Başvurusu'
        verbose_name_plural = 'Burs Başvuruları'
        ordering = ('-bursbasvuru_tarih',)

    def __str__(self):
        return self.bursbasvuru_isim

@receiver(post_delete, sender=Proje)
def submission_delete(sender, instance, **kwargs):
    instance.proje_resim.delete(False)

@receiver(post_delete, sender=Burs)
def submission_delete(sender, instance, **kwargs):
    instance.burs_resim.delete(False)
