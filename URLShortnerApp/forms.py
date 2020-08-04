from django import forms

class URLDataForm(forms.Form):
	EnterURL=forms.CharField(label='Enter U"r URL ', max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Shorten URL Here'}))
