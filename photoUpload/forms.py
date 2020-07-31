from django import forms
from gallery.models import Image

class PhotoUploadForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = [
            'title',
            'date',
            'period_prefix',
            'period',
            'culture',
            'object_type',
            'vase_technique',
            'vase_shape',
            'material',
            'country',
            'artist_or_attribution',
            'associated_building',
            'subject',
            'description',
            'museum_collection',
            'data',
        ]
