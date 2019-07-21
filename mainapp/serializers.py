from rest_framework import serializers
from .models import Proje, Atolye, Burs, Contact, GonulluBasvuru, BursBasvuru

class ProjeSerializer(serializers.Serializer):
    id = serializers.CharField()
    proje_baslik = serializers.CharField()
    proje_icerik = serializers.CharField()
    proje_resim = serializers.ImageField(max_length = None, use_url = False)
    proje_slug = serializers.SlugField(allow_blank = False)

class AtolyeSerializer(serializers.Serializer):
    id = serializers.CharField()
    atolye_baslik = serializers.CharField()
    atolye_donem = serializers.CharField()
    atolye_icerik = serializers.CharField()

class BursSerializer(serializers.Serializer):
    id = serializers.CharField()
    burs_baslik = serializers.CharField()
    burs_icerik = serializers.CharField()
    burs_resim = serializers.ImageField(max_length = None, use_url = False)
    burs_aktiflik = serializers.BooleanField()
    burs_slug = serializers.SlugField(allow_blank = False)

# Returns only if burs_aktiflik is True.
class BursNameSerializer(serializers.Serializer):
    id = serializers.CharField()
    burs_baslik = serializers.CharField()
    burs_aktiflik = serializers.BooleanField()

class DuyuruSerializer(serializers.Serializer):
    id = serializers.CharField()
    duyuru_baslik = serializers.CharField()
    duyuru_mesaj = serializers.CharField()
    duyuru_tarihi = serializers.DateField()
    duyuru_slug = serializers.SlugField()

class ContactSerializer(serializers.Serializer):
    contact_name = serializers.CharField()
    contact_email = serializers.CharField()
    contact_mesaj = serializers.CharField()

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

class GonulluBasvuruSerializer(serializers.Serializer):
    gonullu_isim = serializers.CharField()
    gonullu_email = serializers.CharField()
    gonullu_telefon = serializers.CharField()
    gonullu_calismaalani = serializers.CharField()
    gonullu_baslamatarihi = serializers.CharField()
    gonullu_mesaj = serializers.CharField()

    def create(self, validated_data):
        return GonulluBasvuru.objects.create(**validated_data)

class BursBasvuruSerializer(serializers.Serializer):
    bursbasvuru_isim = serializers.CharField()
    bursbasvuru_email = serializers.CharField()
    bursbasvuru_telefon = serializers.CharField()
    bursbasvuru_basvurulanburs = serializers.CharField()
    bursbasvuru_mesaj = serializers.CharField()

    def create(self, validated_data):
        return BursBasvuru.objects.create(**validated_data)
