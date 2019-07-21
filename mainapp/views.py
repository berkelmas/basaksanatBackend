from rest_framework import generics

from .serializers import ProjeSerializer, AtolyeSerializer, BursSerializer, \
                        ContactSerializer, GonulluBasvuruSerializer, BursBasvuruSerializer, \
                        BursNameSerializer

from .models import Proje, Atolye, Burs, Contact, GonulluBasvuru, BursBasvuru
from .paginations import BursProjePagination, AtolyePagination

class ProjeList(generics.ListAPIView):
    queryset = Proje.objects.all()
    serializer_class = ProjeSerializer
    pagination_class = BursProjePagination

class BursList(generics.ListAPIView):
    queryset = Burs.objects.all()
    serializer_class = BursSerializer
    pagination_class = BursProjePagination

class BursNameList(generics.ListAPIView):
    serializer_class = BursNameSerializer
    def get_queryset(self):
        queryset = Burs.objects.all().filter(burs_aktiflik = True)
        return queryset

class AtolyeList(generics.ListAPIView):
    queryset = Atolye.objects.all()
    serializer_class = AtolyeSerializer
    pagination_class = AtolyePagination

class SingleProje(generics.RetrieveAPIView):
    queryset = Proje.objects.all()
    serializer_class = ProjeSerializer

class SingleBurs(generics.RetrieveAPIView):
    queryset = Burs.objects.all()
    serializer_class = BursSerializer

class AddContact(generics.CreateAPIView):
    serializer_class = ContactSerializer

class AddGonulluBasvuru(generics.CreateAPIView):
    serializer_class = GonulluBasvuruSerializer

class AddBursBasvuru(generics.CreateAPIView):
    serializer_class = BursBasvuruSerializer
