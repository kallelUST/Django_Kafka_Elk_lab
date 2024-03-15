from rest_framework.views import APIView
from .documents import GenericAlertDocument
from .serializer import GenericAlertSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
import json
# Create your views here.

def preprocess_alert_for_twilio(alerts_arr):
    batched_alert = {
        "name":"",
        "description":"",
    }
    for alert in alerts_arr:
        batched_alert["name"] = batched_alert["name"] + " " + alert["name"] if len(batched_alert["name"])>0 else alert["name"]
        batched_alert["description"] = batched_alert["description"] + " " + alert["description"] if len(batched_alert["description"])>0 else alert["description"]
    
    batched_alert['created_at'] = timezone.now()

    return batched_alert

class AlertView(APIView):
    def post(self,request):
        # alert_serializer = GenericAlertSerializer(data=request.data)
        # if alert_serializer.is_valid():
        #     r_body = request.data
        #     new_alert = GenericAlertDocument(name=r_body["name"], description=r_body["description"], 
        #                                      target_team = r_body["target_team"],created_at= timezone.now())
                                             
        #     new_alert.save()
        #     return Response(alert_serializer.data, status=status.HTTP_201_CREATED)
        # return Response(alert_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        # data = json.loads(request.body)
        
        alerts_arr = []
        es = connections.get_connection()
        for item in request.data:
            # print(f'received item is the : {item}')
            alert_serializer = GenericAlertSerializer(data=item)
            if not alert_serializer.is_valid():
                return Response(alert_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            print(alert_serializer.is_valid())
            # new_alert = GenericAlertDocument(name=item["name"], description=item["description"], 
            #                                     target_team = item["target_team"],created_at= timezone.now()).to_dict()
            
            action = {
                    "_op_type":"index",
                    "_index":GenericAlertDocument._index._name,
                    "_source": {
                       "name" :item["name"],
                       "description": item["description"],
                       "target_team": item["target_team"],
                       "created_at":  timezone.now()
                    }
            }
            
          
            alerts_arr.append(action)
            
        bulk(client=es,actions=alerts_arr)
        return Response(status=status.HTTP_201_CREATED)