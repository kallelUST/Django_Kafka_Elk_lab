from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dummy_alert_generator.serializer import Generic_alert_serializer
from .producer_alert_created import ProducerAlertCreated
import json
alertProducer = ProducerAlertCreated()
# Create your views here.
class GeneicAlertView(APIView):
    def post(self,request):
        serializer = Generic_alert_serializer(data=request.data)
        if serializer.is_valid():
            alertProducer.publish(method="create_alert  ",body=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)
