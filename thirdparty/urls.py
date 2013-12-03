from django.conf.urls import patterns, url
#from django.contrib.auth.decorators import login_required
from thirdparty.views import LicenseIndex, ThirdPartyComponentIndex

urlpatterns = patterns('',
    url(r'licenses/$',LicenseIndex.as_view(), name="licindex"),
    url(r'components/$',ThirdPartyComponentIndex.as_view(), name="thirdpartyindex"),
    #url(r'^(?P<pk>\d+)/$', get_detail, name="detail"),
)