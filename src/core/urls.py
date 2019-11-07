from django.urls import path
from .views import ListCeletialBodies

urlpatterns = [
    path("list", ListCeletialBodies.as_view(), name='list'),
]
