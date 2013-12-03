from django.contrib import admin

from thirdparty.models import ThirdPartyComponent, License


admin.site.register(ThirdPartyComponent)
admin.site.register(License)