from django import forms
from .models import Product
from .models import Category, Brand, Color

class StoreForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'product_name', 'price', 'category', 'brand', 'color']

class AdvancedSearchForm(forms.Form):
    min_price = forms.IntegerField(
        required=False,
        label='Минимальная цена',
        widget=forms.NumberInput(attrs={'placeholder': 'От'})
    )
    max_price = forms.IntegerField(
        required=False,
        label='Максимальная цена',
        widget=forms.NumberInput(attrs={'placeholder': 'До'})
    )
    Category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Категория',
        widget=forms.CheckboxSelectMultiple
    )
    Brand = forms.ModelMultipleChoiceField(
        queryset=Brand.objects.all(),
        required=False,
        label='Бренд',
        widget=forms.CheckboxSelectMultiple
    )
    Color = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),
        required=False,
        label='Цвет',
        widget=forms.CheckboxSelectMultiple
    )


class SearchForm(forms.Form):
    product_name = forms.CharField(
        label='',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Искать товары', 'class': 'search-input'}))