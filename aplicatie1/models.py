from django.db import models

# Create your models here.
from aplicatie2.models import Location

MARCA_CHOICES = (
    ('Mercedes', 'MERCEDES'),
    ('Audi', 'AUDI'),
    ('Opel', 'OPEL'),
    ('Mazda', 'MAZDA'),
    ('BMW', 'BMW'),
    ('Volkswagen', 'VOLKSWAGEN'),
    ('Ford', 'FORD'),
    ('Dacia', 'DACIA'),
    ('Skoda', 'SKODA'),
    ('Seat', 'SEAT'),
    ('Honda', 'HONDA'),
    ('Peugeot', 'PEUGEOT'),
)

COMBUSTIBIL_CHOICES = (
    ('DIESEL', 'DIESEL'),
    ('BENZINA', 'BENZINA'),
    ('HYBRID', 'HYBRID'),
    ('ELECTRIC', 'ELECTRIC'),
)

CUTIE_CHOICES = (
    ('AUTOMATA', 'AUTOMATA'),
    ('MANUALA', 'MANUALA'),
)

class Car(models.Model):

    marca = models.CharField(choices=MARCA_CHOICES,max_length=45)
    model = models.CharField(max_length=45)
    an_aparitie = models.IntegerField()
    combustibil = models.CharField(choices=COMBUSTIBIL_CHOICES,max_length=45)
    motorizare = models.FloatField()
    consum = models.FloatField()
    cai_putere = models.IntegerField()
    cutie = models.CharField(choices=CUTIE_CHOICES, max_length=45, null=True, blank=True)
    poza = models.ImageField(upload_to='cars')
    pret = models.CharField(max_length=20)
    active = models.BooleanField(default=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,  null=True, blank=True)

    def __str__(self):
        return f"{self.marca} - {self.model} - {self.an_aparitie} - {self.combustibil} - {self.motorizare} - {self.cai_putere} - {self.consum} - {self.pret} "