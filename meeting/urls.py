from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from meeting import views

urlpatterns = patterns('',
  url(r"^/?$", TemplateView.as_view(template_name = "meeting/home.html"), name = "index"),
  url(r"^api/users/(?P<pk>[\d]+)$", views.UserDetail.as_view(), name = "user-detail"),
  url(r"^api/meeting/$", views.MeetingList.as_view(), name = "meeting-list"),
  url(r"^api/meeting/(?P<mhash>[a-f0-9]+)$", views.MeetingDetail.as_view(), name = "meeting-detail"),
)
