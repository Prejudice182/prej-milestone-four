from django.forms import ModelForm
from .models import BillingAddress


class BillingForm(ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['street_address1', 'street_address2',
                  'town_or_city', 'county_or_state', 'country', 'postcode']
