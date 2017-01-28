from django.conf.urls import url
from simpleavatar.views import change

urlpatterns = [
    url('^change/$', change, name='avatar_change'),
]
