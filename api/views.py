from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.queue_datastructure import Queue
import json
from twilio.rest import Client

# initialize a 'Doe' family
queue = Queue(mode='FIFO')

"""
The MembersView will contain the logic on how to:
 GET, POST, PUT or delete family members
"""
class QueueView(APIView):
    def get(self, request):
        result = queue.dequeue()
        # fill this method and update the return
        return Response(result,status=status.HTTP_200_OK)

    def post(self, request):
        # add a new member to the queue
        item = request.data
        result = queue.enqueue(item)
        return Response(result, status=status.HTTP_200_OK)

class QueueAllView(APIView):
    def get(self, request):
        result = queue.get_all()
        return Response(result, status=status.HTTP_200_OK)
