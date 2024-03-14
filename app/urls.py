from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_clp.views import JSONView, myView

# Crie um roteador
router = DefaultRouter()

# Registre sua viewset com o roteador
router.register(r'clp', JSONView) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template/', myView, name='template'),
    # Inclua as URLs geradas pelo roteador
    path('', include(router.urls)),
]
