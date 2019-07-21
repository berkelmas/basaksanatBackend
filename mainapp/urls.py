from django.urls import path
from .views import ProjeList, BursList, AtolyeList, SingleProje, SingleBurs, \
                    AddContact, AddGonulluBasvuru, AddBursBasvuru, BursNameList

urlpatterns = [
    path('projeler', ProjeList.as_view(), name="projeler"),
    path('burslar', BursList.as_view(), name="burslar"),
    path('aktifburslar', BursNameList.as_view(), name="aktifburslar"),
    path('atolyeler', AtolyeList.as_view(), name="atolyeler"),
    path('singleproje/<int:pk>/', SingleProje.as_view(), name="singleproje"),
    path('singleburs/<int:pk>', SingleBurs.as_view(), name="singleburs"),
    path('addcontact', AddContact.as_view(), name="addcontact"),
    path('addgonullubasvuru', AddGonulluBasvuru.as_view(), name="addgonullubasvuru"),
    path('addbursbasvuru', AddBursBasvuru.as_view(), name="addbursbasvuru")
]
