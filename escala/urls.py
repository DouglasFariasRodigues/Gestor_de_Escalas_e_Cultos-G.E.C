from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()


#Registro de rotas
router.register(r'Obreiros', views.ObreirosViewSet, basename='Obreiros')
router.register(r'Locais', views.Local_ViewSet, basename='Locais')
router.register(r'NatCultos', views.NatCultoViewSet, basename='NatCultos')
router.register(r'Cultos', views.CultoViewSet, basename='Cultos')
router.register(r'Escalas', views.EscalaViewSet, basename='Escalas')
router.register(r'EscalaItems', views.EscalaItemViewSet, basename='EscalaItems')
router.register(r'Indisponibilidades', views.IndisponibilidadeViewSet, basename='Indisponibilidades')

#Urls da API
urlpatterns = [
    path('', include(router.urls)),
]