from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from meeting.serializers import UserSerializer, MeetingSerializer
from meeting.models import Meeting
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.response import Response

class UserDetail(RetrieveAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()


class MeetingList(ListAPIView):
  serializer_class = MeetingSerializer
  queryset = Meeting.objects.all()
  lookup_field = "mhash"


class MeetingDetail(RetrieveAPIView):
  serializer_class = MeetingSerializer
  queryset = Meeting.objects.all()
  lookup_field = "mhash"
  
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    
    return Response(serializer.data)
