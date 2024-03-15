import json
from confluent_kafka import Producer
import socket
# Must be taken out of the box
topic='topic_alert_created'
class ProducerAlertCreated:
    def __init__(self) -> None:
        # muste be taken out of the box        
        conf = {'bootstrap.servers': "localhost:9092",'client.id': socket.gethostname()}
        self.producer = Producer(conf)

    # This method will be called inside view for sending Kafka message
    def publish(self,method, body):
        self.producer.produce(topic, key="key.alert.created", value=json.dumps(body))