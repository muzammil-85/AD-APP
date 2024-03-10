from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['ad_name','image_ad', 'video_ad', 'stand', 'ad_shown_duration']

