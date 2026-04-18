from django import forms


class CrimeFilterForm(forms.Form):
    metric = forms.CharField(required=False, label='Metric')
    year_from = forms.IntegerField(required=False, label='Year From')
    year_to = forms.IntegerField(required=False, label='Year To')