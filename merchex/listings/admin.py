from django.contrib import admin
from listings.models import Band, Listings

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('description', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listings, ListingsAdmin)