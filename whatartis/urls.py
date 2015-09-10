
from django.conf.urls import include, url
from django.contrib import admin

from whatisitfor.views import WhatArtIs, WhatIsItFor


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^/$', WhatIsItFor.as_view(), name='what-is-it-for'),
    url(r'^o/(?P<pk>[-\d]+)/$', WhatArtIs.as_view(), name='what-art-is'),
]
