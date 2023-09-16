from django import forms
from .models import Purchase, PurchaseDetail
from django.forms import modelformset_factory, inlineformset_factory


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['code']  # Add other fields as needed


class PurchaseDetailForm(forms.ModelForm):
    class Meta:
        model = PurchaseDetail
        fields = ['product_variation', 'quantity_purchased']  # Add other fields as needed


PurchaseDetailFormSet = modelformset_factory(
    PurchaseDetail,
    form=PurchaseDetailForm,
    # extra=3,  # no need to set, it just produce errors it user tries to delete the extra form-set. Let the user click add/delete button by himself
)


PurchaseFormSet = inlineformset_factory(
    Purchase,
    PurchaseDetail,
    form=PurchaseDetailForm,
    fields=['product_variation', 'quantity_purchased'],
    extra=0,  # Set the number of empty forms to display
)
