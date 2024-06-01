from django.urls import path
from .views import societe_aviation, detail_societe_aviation, Societes_aviation, AddVoyage, livraison, immobilier, decoration, assurance, mecanique, evenement, formation, contact

app_name='other'

urlpatterns = [
    path('sociétés_aviation/', societe_aviation, name='societe_aviation'),
    path('<str:slug>/trajets/', detail_societe_aviation, name='trajets'),
    path('back/voyage/', Societes_aviation.as_view(), name='voyage'),
    path('back/add/voyage/', AddVoyage.as_view(), name='add-voyage'),
    path('livraison/', livraison, name='livraison'),
    path('immobilier/', immobilier, name='immobilier'),
    path('decoration/', decoration, name='decoration'),
    path('assurance/', assurance, name='assurance'),
    path('evenement/', evenement, name='evenement'),
    path('mecanique/', mecanique, name='mecanique'),
    path('formation/', formation, name='formation'),
    path('contact/', contact, name='contact'),
]
