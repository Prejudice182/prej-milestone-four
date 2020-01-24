from django import forms
from crispy_forms.bootstrap import StrictButton, FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class QuantitySelectForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, widget=forms.Select(
        choices=[(i, i) for i in range(1, 11)]))


class OrderByForm(forms.Form):
    ORDER_BY_CHOICES = [
        ('price', 'Price: Low to High'),
        ('priced', 'Price: High to Low'),
        ('name', 'Name: A to Z'),
        ('named', 'Name: Z to A'),
        ('pk', 'Id: Ascending'),
        ('pkd', 'Id: Descending'),
    ]
    order = forms.ChoiceField(choices=ORDER_BY_CHOICES,
                              required=False, label='')

    def __init__(self, *args, **kwargs):
        super(OrderByForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline justify-content-center justify-content-sm-end'
        self.helper.form_method = 'get'
        self.helper.layout = Layout(FieldWithButtons(
            'order', StrictButton('Sort', type='submit', css_class='btn-primary')))
