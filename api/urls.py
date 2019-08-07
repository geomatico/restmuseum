from django.conf.urls import url

from api.views import UniqueValuesRestApi
from api.views import TaxonRestApi

urlpatterns = [
    url('unique/(?P<field>.+)/$', UniqueValuesRestApi.as_view(),
        name='getuniquevalues'),
    url('taxon/(?P<taxon_id>.+)/(?P<taxon_level>.+)/$', TaxonRestApi.as_view(),
        name='gettaxoncount'),
]
