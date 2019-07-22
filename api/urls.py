from django.conf.urls import url

from api.views import ApiExample
from api.views import TaxonRestApi

urlpatterns = [
    url('family/(?P<family_id>.+)/basisofrecord/(?P<basis_of_record>.+)/$', ApiExample.as_view(),
        name='getfamily'),
    url('taxon/(?P<taxon_id>.+)/(?P<taxon_level>.+)/$', TaxonRestApi.as_view(),
        name='gettaxoncount'),
]
