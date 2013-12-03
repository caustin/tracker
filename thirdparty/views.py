from django.views.generic import ListView
from thirdparty.models import License, ThirdPartyComponent


class LicenseIndex(ListView):

    model = License
    context_object_name = 'license_list'
    queryset = License.objects.order_by('name')
    paginate_by = 20

    template_name = "license_index.html"


class ThirdPartyComponentIndex(ListView):

    model = ThirdPartyComponent
    context_object_name = 'third_party_list'
    queryset = ThirdPartyComponent.objects.order_by('name')
    paginate_by = 20

    template_name = "third_party_index.html"