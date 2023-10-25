from django.db import models


from django.core.validators import MaxValueValidator, MinValueValidator
class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(default = '',max_length=1000)
    year_formed = models.fields.IntegerField(default = 2000,
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    genre = models.fields.CharField(default = 'HH',choices=Genre.choices, max_length=5)

    