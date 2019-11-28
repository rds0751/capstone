from django import forms

language_choices = [
    'English',
    'Hindi',
    'French',
    'Spanish',
    'German'
]


class TranslateForm(forms.Form):
    translate = forms.CharField()
    language = forms.CharField(widget=forms.Select(choices=language_choices))
