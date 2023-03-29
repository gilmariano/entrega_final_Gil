from django import forms
from AppPesca.models import Pesca

class PostForm(forms.ModelForm):
    class Meta:
        model = Pesca
        fields = '__all__'

class SearchForm(forms.Form):
    criterio = forms.CharField(max_length=100)