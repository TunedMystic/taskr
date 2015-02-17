from django.contrib.auth import get_user_model
from rest_framework import serializers
from meeting.models import Meeting

from django.contrib.auth import get_user_model
User = get_user_model()


class MeetingSerializer(serializers.ModelSerializer):
  url = serializers.HyperlinkedIdentityField(lookup_field = "mhash", view_name = "meeting:meeting-detail")
  meeting_id = serializers.ReadOnlyField(source = "mhash")
  
  class Meta:
    model = Meeting
    fields = ("meeting_id", "person", "company", "date", "location", "priority", "notes", "url")
  
  def validate_person(self, value):
    print "validating person"
    return value


class UserSerializer(serializers.ModelSerializer):
  meetings = MeetingSerializer(many = True)
  
  class Meta:
    model = User
    fields = ("username", "email", "meetings")
