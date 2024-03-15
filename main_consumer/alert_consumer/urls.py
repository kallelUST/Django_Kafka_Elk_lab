from django.urls import path
from .views import AlertView

urlpatterns = [
    path('alerts',AlertView.as_view())
]
