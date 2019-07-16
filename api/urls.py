from django.conf.urls import url

from api.views import GetThingsFromDataBase

urlpatterns = [
    url('family/(?P<family_id>.+)/basisofrecord/(?P<basis_of_record>.+)/$', GetThingsFromDataBase.as_view(),
        name='getfamily'),
]
