from django.contrib import admin

from thirdparty.models import (
    ThirdPartyComponent,
    License,
    Component,
    Vulnerability
)


admin.site.register(ThirdPartyComponent)
admin.site.register(License)
admin.site.register(Component)
admin.site.register(Vulnerability)