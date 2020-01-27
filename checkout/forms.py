from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from django.forms import ModelForm
from .models import BillingAddress


class BillingForm(ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['street_address1', 'street_address2',
                  'town_or_city', 'county_or_state', 'country', 'postcode']

    def __init__(self, *args, **kwargs):
        super(BillingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('street_address1'),
            Field('street_address2'),
            Div(
                Field('town_or_city', wrapper_class='col-md-6'),
                Field('county_or_state', wrapper_class='col-md-6'),
                css_class='form-row'
            ),
            Div(
                Field('country', wrapper_class='col-md-6'),
                Field('postcode', wrapper_class='col-md-6'),
                css_class='form-row'
            ),
            StrictButton('Next', type='submit', css_class='rust-button float-right')
        )
