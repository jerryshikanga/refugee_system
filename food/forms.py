from django import forms
from . models import Food


class IncreaseReservesForm(forms.Form):
    quantity = forms.IntegerField(required=True)

    def increase_reserves(self, food: Food):
        quantity = self.data['quantity']
        food.quantity += int(quantity)
        food.save()
        return True