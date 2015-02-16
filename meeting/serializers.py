from django.contrib.auth import get_user_model
from rest_framework import serializers
from meeting.models import Meeting

from django.contrib.auth import get_user_model
User = get_user_model()

class MeetingSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Meeting
    fields = ("id", "user", "person", "company", "date", "location", "priority", "notes")
  
  def save()


class UserSerializer(serializers.ModelSerializer):
  meetings = MeetingSerializer(many = True)
  
  class Meta:
    model = User
    fields = ("id", "username", "email", "meetings")
