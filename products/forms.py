from django import forms


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
    order = forms.ChoiceField(choices=ORDER_BY_CHOICES, label='Sort Products')
    