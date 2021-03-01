from django import forms


class ProductSearch(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'ui-input-field ui-input-field--cleanable',
        'placeholder': 'نام محصول یا برند مورد نظر را بنویسید…',
    }))
