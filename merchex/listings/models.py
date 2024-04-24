from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Band(models.Model):

	class Genre(models.TextChoices):
		HIP_HOP = 'HH'
		SYNTH_POP = 'SP'
		ALTERNATIVE_ROCK = 'AR'
		JAZZ = 'JA'
		VARIETE_FR = 'VF'

	name = models.fields.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	genre = models.fields.CharField(choices=Genre.choices, max_length=5)
	biography = models.fields.CharField(max_length=1000)
	year_formed = models.fields.IntegerField(
		validators=[MinValueValidator(1900), MaxValueValidator(2024)]
	)
	active = models.fields.BooleanField(default=True)
	official_homepage = models.fields.URLField(null=True, blank=True)

#def ecriture du nom ds la bd
	def __str__(self):
		return f"{self.name}"

##btn pr voir sur le site ds la bd
	def get_absolute_url(self):
		return reverse("band", kwargs={"slug": self.slug})

class Listing(models.Model):
	class ListingType(models.TextChoices):
		RECORDS = 'R'
		CLOTHING = 'C'
		POSTERS = 'P'
		MISC = 'M'

	title = models.fields.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	description = models.fields.CharField(max_length=1000)
	sold = models.fields.BooleanField(default=False)
	year_formed = models.fields.IntegerField(
		null=True,
		validators=[MinValueValidator(1900), MaxValueValidator(2024)]
	)
	type = models.fields.CharField(choices=ListingType.choices, max_length=5)
	band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL) #ajout cle etrangere ds model Listings(issut de la class band)

	#définir le champ band comme nul en utilisant models.SET_NULL,

	#définir le champ band à sa valeur par défaut en utilisant models.SET_DEFAULT,

	#supprimer l'objet Listing en utilisant models.CASCADE,

	#et d'autres paramètres plus complexes que vous pouvez trouver décrits dans la documentation de Django.

	#Nous ne voulons pas supprimer l'objet Listing si un Band est supprimé, nous utiliserons donc SET_NULL.
	
	#def ecriture du nom ds la bd
	def __str__(self):
		return f"{self.title}"
