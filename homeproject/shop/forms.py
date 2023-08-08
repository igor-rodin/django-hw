from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128,
        label="Название",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Название товара"}
        ),
    )
    description = forms.CharField(
        label="Описание", widget=forms.Textarea(attrs={"class": "form-control"})
    )
    price = forms.FloatField(
        label="Цена", widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    image = forms.ImageField(label="Изображение товара")

    class Meta:
        model = Product
        fields = ["title", "description", "price", "image"]
