from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm, AddBandForm, AddListingForm
from django.core.mail import send_mail

def band_list(request):
	bands = Band.objects.all()
	return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
	#return render(request, 'listings/band_detail.html',	{'id': id})
	band = Band.objects.get(id=id)
	return render(request, 'listings/band_detail.html',	{'band': band})

def about_us(request):
	#return HttpResponse('<h1>A propos</h1> <p>Nous adorons march!</p>')
	return render(request, 'listings/about_us.html')

def listing(request):
	listings = Listing.objects.all()
	return render(request, 'listings/listing.html', {'listings': listings})

def listing_detail(request, id):
	listing = Listing.objects.get(id=id)
	return render(request, 'listings/listing_detail.html',	{'listing': listing})

def contactUs(request):
	#print('La methode requete est : ', request.method)
	#print('Les donnes POST sont : ', request.POST)
	if request.method == 'POST': #fill form
		form = ContactUsForm(request.POST)
		if form.is_valid():
			send_mail(
				subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
				message=form.cleaned_data['message'],
				from_email=form.cleaned_data['email'],
				recipient_list=['admin@merchex.xyz'],
			)
		return redirect('email-sent')
	else: #request GET -> empty form
		form = ContactUsForm()
	return render(request, 'listings/contact_us.html', {'form': form}) #pass this form at gabarit

def email_sent(request):
	return render(request, 'listings/email_sent.html')

def band_add(request):
	if request.method == 'POST':
		form = AddBandForm(request.POST)
		if form.is_valid():
			band = form.save()
			return redirect('band-detail', band.id)
	else:
		form = AddBandForm()
	return render(request, 'listings/band_add.html', {'form': form})

def listing_add(request):
	if (request.method == 'POST'):
		form = AddListingForm(request.POST)
		if form.is_valid():
			listing = form.save()
			return redirect('listing')
	else:
		form = AddListingForm()
	return render(request, 'listings/listing_add.html', {'form': form})

def band_update(request, id):
	band = Band.objects.get(id=id)
	if request.method == 'POST':
		form = AddBandForm(request.POST, instance=band)
		if form.is_valid():
			form.save()
			return redirect('band-detail', band.id)
	else:
		form = AddBandForm(instance=band)
	return render(request, 'listings/band_update.html', {'form': form})

def listing_update(request, id):
	listing = Listing.objects.get(id=id)
	if request.method == 'POST':
		form = AddListingForm(request.POST, instance=listing)
		if form.is_valid():
			form.save()
			return redirect('listing-detail', listing.id)
	else:
		form = AddListingForm(instance=listing)
	return render(request, 'listings/listing_update.html', {'form': form})

def band_delete(request, id):
	band = Band.objects.get(id=id)
	if request.method == 'POST':
		band.delete()
		return redirect('band-list')
	return render(request, 'listings/band_delete.html', {'band': band})

def listing_delete(request, id):
	listing = Listing.objects.get(id=id)
	if request.method == 'POST':
		listing.delete()
		return redirect('listing')
	return render(request, 'listings/listing_delete.html',	{'listing': listing})
