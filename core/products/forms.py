from django import forms
from .models import Comment as ProductVariationComment

class ProductVariationCommentForm(forms.ModelForm):
    class Meta:
        model = ProductVariationComment
        fields = ['content']
