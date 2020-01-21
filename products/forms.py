from django import forms


class QuantitySelectForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, widget=forms.Select(
        choices=[(i, i) for i in range(1, 11)]))
