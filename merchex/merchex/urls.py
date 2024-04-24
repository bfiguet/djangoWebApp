"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.band_list, name='band-list'),
	path('bands/<int:id>/', views.band_detail, name='band-detail'),
	path('band_add/', views.band_add, name='band-add'),
	path('band_update/<int:id>/', views.band_update, name='band-update'),
	path('band_delete/<int:id>/', views.band_delete, name='band-delete'),
	path('about_us/', views.about_us, name='about-us'),
	path('listing/', views.listing, name='listing'),
	path('listing/<int:id>', views.listing_detail, name='listing-detail'),
	path('listing_add/', views.listing_add, name='listing-add'),
	path('listing_update/<int:id>/', views.listing_update, name='listing-update'),
	path('listing_delete/<int:id>/', views.listing_delete, name='listing-delete'),
	path('contact/', views.contactUs, name='contact-us'),
	path('email-sent/', views.email_sent, name='email-sent'),
]
