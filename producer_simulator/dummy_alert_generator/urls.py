from django.urls import path
from .views import GeneicAlertView

urlpatterns = [
    path('alerts', GeneicAlertView.as_view())
]
