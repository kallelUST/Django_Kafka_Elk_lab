import json
import sys 
import threading
from confluent_kafka import Consumer
from confluent_kafka import KafkaError
from confluent_kafka import KafkaException
import time 
import requests
#We want to run thread in an infinite loop
running=True
conf = {'bootstrap.servers': "localhost:9092",
        'auto.offset.reset': 'smallest',
        'group.id': "alert_group"}
#Topic
topic='topic_alert_created'


class AlertListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # Create consumer
        self.consumer = Consumer(conf)
   
        
    def run(self):
        print ('Inside alert Service :  Created Listener ')
        try:
            #Subcribe to topic
            self.consumer.subscribe([topic])
            # Need to add it dynamically
            
            while running:
                message_list = []
                while running:
                    msg = self.consumer.poll(timeout=1.0)
                    if msg is None:break
                    if msg.error():
                        if msg.error().code() == KafkaError._PARTITION_EOF:
                            print('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                    else:
                         #We are going to handle the message
                        print('---------> Got message Sending email.....')
                        message = json.loads(msg.value().decode('utf-8'))
                        print(message)
                        message_list.append(message)
                # DO the API call
                print(json.dumps(message_list))
                if(len(message_list)):requests.post("http://localhost:8000/api/alerts",json=message_list)
                # Sleep for x minutes 
                time.sleep(15)  
        finally:
        # Close down consumer to commit final offsets.
            self.consumer.close()
    
   