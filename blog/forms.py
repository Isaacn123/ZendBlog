from django import forms
from  .models import Image


class ImageForm(forms.ModelForm):
    """Form for the Image Model Upload"""
    class Meta:
        model = Image
        fields = ('title','image')