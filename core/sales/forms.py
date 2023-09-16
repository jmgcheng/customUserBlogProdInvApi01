from django import forms
from .models import Sale, SaleDetail
from django.forms import modelformset_factory, inlineformset_factory


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['code']  # Add other fields as needed


class SaleDetailForm(forms.ModelForm):
    class Meta:
        model = SaleDetail
        fields = ['product_variation', 'quantity_released']  # Add other fields as needed


SaleDetailFormSet = modelformset_factory(
    SaleDetail,
    form=SaleDetailForm,
    # extra=3,  # no need to set, it just produce errors it user tries to delete the extra form-set. Let the user click add/delete button by himself
)


SaleFormSet = inlineformset_factory(
    Sale,
    SaleDetail,
    form=SaleDetailForm,
    fields=['product_variation', 'quantity_released'],
    extra=0,  # Set the number of empty forms to display
)
