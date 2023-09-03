# -*- coding: utf-8 -*-
from django.urls import path

from aldryn_events.views import event_list, event_dates, event_list_archive, event_detail, reset_event_registration

urlpatterns = [
    path(r'', event_list, name='events_list'),
    path(r'get-dates/', event_dates, name='get-calendar-dates'),
    path(r'get-dates/(?P<year>[0-9]+)/(?P<month>[0-9]+)/', event_dates, name='get-calendar-dates'),
    path(r'(?P<year>\d{4})/', event_list, name='events_list-by-year'),
    path(r'(?P<year>\d{4})/(?P<month>\d{1,2})/', event_list, name='events_list-by-month'),
    path(r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/', event_list, name='events_list-by-day'),
    path(r'archive/', event_list_archive, name='events_list_archive'),
    path(r'archive/(?P<year>\d{4})/', event_list_archive, name='events_list_archive-by-year'),
    path(r'archive/(?P<year>\d{4})/(?P<month>\d{1,2})/', event_list_archive, name='events_list_archive-by-month'),
    path(r'(?P<slug>[\w_-]+)/', event_detail, name='events_detail'),
    path(r'(?P<slug>[\w_-]+)/reset/', reset_event_registration, name='events_registration_reset'),
]
