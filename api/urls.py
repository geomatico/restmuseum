from django.conf.urls import url

from api.views import UniqueValuesRestApi
from api.views import TaxonRestApi
from api.views import StatsRestApi
from api.views import SearchRestApi
from api.views import MinmaxYearsRestApi

urlpatterns = [
    url('years/$', MinmaxYearsRestApi.as_view(),
        name='getminmaxyears'),
    url('search/(?P<terms>.+)/$', SearchRestApi.as_view(),
        name='getminmaxyears'),
    url('unique/(?P<field>.+)/$', UniqueValuesRestApi.as_view(),
        name='getuniquevalues'),
    url('stats/(?P<type>.+)/(?P<taxon_id>.+)/(?P<taxon_level>.+)/$', StatsRestApi.as_view(),
        name='gettaxoncount'),
    url('taxon/(?P<taxon_id>.+)/(?P<taxon_level>.+)/$', TaxonRestApi.as_view(),
        name='gettaxoncount'),
]
