from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    TEMPERATURE_CHOICES = [
        ('hot', 'Гарячий'),
        ('cold', 'Холодний'),
    ]

    SIZE_CHOICES = [
        ('S', 'Маленький (180 мл)'),
        ('M', 'Середній (250 мл)'),
        ('L', 'Великий (350 мл)'),
    ]

    temperature = forms.ChoiceField(
        choices=TEMPERATURE_CHOICES,
        label='Температура'
    )
    size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        initial='M',
        label='Розмір'
    )
    quantity = forms.IntegerField(
        min_value=1,
        max_value=10,
        initial=1,
        label='Кількість'
    )

    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone', 'customer_email',
                  'address', 'notes', 'temperature', 'size', 'quantity']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
        labels = {
            'customer_name': "Ім'я*",
            'customer_phone': 'Телефон*',
            'customer_email': 'Email',
            'address': 'Адреса доставки*',
            'notes': 'Примітки до замовлення'
        }
