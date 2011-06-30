from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^titlecovers/(\d(?:\d|-)+\d)/detailurl', 'titlecovers.views.detailurl'),
    (r'^titlecovers/(\d(?:\d|-)+\d)/(\w+)', 'titlecovers.views.imgurl'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
