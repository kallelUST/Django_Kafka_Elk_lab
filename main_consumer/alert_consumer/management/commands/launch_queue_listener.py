from django.core.management.base import BaseCommand
from alert_consumer.alert_kafka_listener import AlertListener
class Command(BaseCommand):
    help = 'Launches Listener for user_created message : Kafka'
    def handle(self, *args, **options):
        td = AlertListener()
        td.start()
        self.stdout.write("Started Consumer Thread")