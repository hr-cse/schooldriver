from django.conf.urls import *
from views import *

urlpatterns = patterns('',
    (r'^enroll/(?P<id>\d+)$', schedule_enroll),
)
