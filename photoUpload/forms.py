from django import forms
from gallery.models import Image

class PhotoUploadForm(forms.ModelForm):
    date = forms.CharField(
        label='Specific Date(s)',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 142 CE, 420-410 BCE, 2nd century BCE','name': 'Specific Date(s)'})
    )

    class Meta:
        model = Image
        fields = [
            'title',
            'date',
            'period',
            'period_prefix',
            'culture',
            'object_type',
            'vase_technique',
            'vase_shape',
            'material',
            'artist_or_attribution',
            'country',
            'associated_building',
            'associated_site',
            'subject',
            'description',
            'museum_collection',
            'data',
        ]
        labels = {'date': 'Specific Date(s)'}
