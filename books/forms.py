from django import forms 
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['description']
        widget = {
            'description': forms.Textarea(attrs={'class': 'textarea textarea-bordered'})
        }