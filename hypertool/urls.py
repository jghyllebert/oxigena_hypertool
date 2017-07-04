from django.conf.urls import url
from django.contrib import admin

from clients.views import Authenticate


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url (r'^api/authenticate/$', Authenticate.as_view())
]
