"""blueflamingo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from blueflamingoapi.views.pump_house_parameters_view import PumphouseParametersView
from blueflamingoapi.views.salinity_view import SalinityView
from blueflamingoapi.views.hardness_view import HardnessView
from blueflamingoapi.views.free_chlorine_view import FreeChlorineView
from blueflamingoapi.views.total_chlorine_view import TotalChlorineView
from blueflamingoapi.views.filter_pressure_view import FilterPressureView
from blueflamingoapi.views.cyanuric_acid_view import CyanuricAcidView
from blueflamingoapi.views.alkalinity_view import AlkalinityView
from blueflamingoapi.views import PumpHouseView, PhView
from django.contrib import admin
from django.urls import path
from blueflamingoapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'pumphouse', PumpHouseView, 'pumphouse')
router.register(r'alkalinity', AlkalinityView, 'alkalinity')
router.register(r'cyanuricacid', CyanuricAcidView, 'cyanuricacid')
router.register(r'filterpressure', FilterPressureView, 'filterpressure')
router.register(r'freechlorine', FreeChlorineView, 'freechlorine')
router.register(r'hardness', HardnessView, 'hardness')
router.register(r'ph', PhView, 'ph')
router.register(r'salinity', SalinityView, 'salinity')
router.register(r'pumphousedata', PumphouseParametersView, 'pumphousedata')
router.register(r'totalchlorine', TotalChlorineView, 'totalchlorine')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
