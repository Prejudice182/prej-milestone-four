from django import forms
from crispy_forms.bootstrap import StrictButton, FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class QuantitySelectForm(forms.Form):
    '''
    Display a quantity field as a select dropdown, with values ranging from 1-10
    '''
    quantity = forms.IntegerField(min_value=1, max_value=10, widget=forms.Select(
        choices=[(i, i) for i in range(1, 11)]))


class OrderByForm(forms.Form):
    '''
    Display a choice field for sorting a list of products by various means
    '''
    ORDER_BY_CHOICES = [
        ('pk', 'Id: Ascending'),
        ('pkd', 'Id: Descending'),
        ('price', 'Price: Low to High'),
        ('priced', 'Price: High to Low'),
        ('name', 'Name: A to Z'),
        ('named', 'Name: Z to A'),
    ]
    order = forms.ChoiceField(choices=ORDER_BY_CHOICES,
                              required=False, label='')

    def __init__(self, *args, **kwargs):
        # Set up the form using Crispy Forms layout
        super(OrderByForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline justify-content-center justify-content-sm-end'
        self.helper.form_method = 'get'
        self.helper.layout = Layout(Field(
            'order', css_class="mx-2"), StrictButton('Sort', type='submit', css_class='rust-button'))
