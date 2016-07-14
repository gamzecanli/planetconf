from django import forms

from .models import Planet,Blogger

class PlanetForm(forms.ModelForm):

    class Meta:
        model = Planet
        fields = '__all__'

class BloggerForm(forms.ModelForm):

    class Meta:
        model = Blogger
        fields = '__all__'

