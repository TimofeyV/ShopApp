from django import forms
from.models import Product

class UserForm(forms.Form):
    name = forms.CharField(max_length=200, label='Логин')
    email = forms.EmailField(label='Электронная почта')
    phone = forms.CharField(max_length=15, label='Телефон')
    address = forms.CharField(max_length=200, label='Адрес')


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id','image',)