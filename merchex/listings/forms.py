from django import forms
from listings.models import Band, Listing

class ContactUsForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField(required=False)
	message = forms.CharField(max_length=1000)

class AddBandForm(forms.ModelForm):
	class Meta: #cpy class Band
		model = Band #name of cpy
		#fields = '__all__' #cpy all
		exclude = ('slug', 'active', 'official_homepage')

class AddListingForm(forms.ModelForm):
	class Meta:
		model = Listing
		exclude = ('slug', 'sold')
