from rest_framework.serializers import ModelSerializer
from alert_consumer.models import GenericAlert
class GenericAlertSerializer(ModelSerializer):
    class Meta:
        model = GenericAlert
        fields = (
            "name",
            "description",
            "target_team",
        )
 