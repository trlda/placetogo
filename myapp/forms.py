from django import forms

class NewPlaceForm(forms.Form):
    place = forms.CharField(max_length=200, label='New Place')
    discription = forms.CharField(max_length=200, label="About place", widget=forms.Textarea)
    priority = forms.IntegerField(min_value=1, max_value=5)