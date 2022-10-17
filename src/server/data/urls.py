from django.urls import include, path
from rest_framework import routers

import data.views as views

router = routers.DefaultRouter()
router.register(r"light_intensity_points", views.LightIntensityPointViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
