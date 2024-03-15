from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Field
from .models import GenericAlert

@registry.register_document
class GenericAlertDocument(Document):

    class Index:
        name= "meerkat_alerts"
        settings = {
            "number_of_shards" : 1,
            "number_of_replicas":1
        }

    class Django:
        model = GenericAlert
        fields = [
            "name",
            "description",
            "target_team",
            "created_at"
        ]