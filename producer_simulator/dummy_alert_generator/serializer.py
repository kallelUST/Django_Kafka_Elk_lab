from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from dummy_alert_generator.models import Generic_alert

class Generic_alert_serializer(ModelSerializer):
    class Meta:
        model = Generic_alert
        fields = (
            "name",
            "description",
            "target_team",
            "created_at"
        )
 
    