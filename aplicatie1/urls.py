from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from aplicatie1 import views

app_name = 'carApp'

urlpatterns = [
    path('', views.CarsView.as_view(), name='lista_masini'),
    path('addCar/', views.CreateCarsView.as_view(), name='addCar'),
    path('<int:pk>/updateCar/', views.UpdateCarsView.as_view(), name='updateCar'),
    path('<int:pk>/deleteCar/', views.delete_cars, name='deleteCar'),
    path('<int:pk>/activateCar/', views.activate_cars, name='activateCar'),
    path('inactiveCars', views.CarsInactiveView.as_view(), name='inactiveCars'),
    path('searchCars/', views.search_cars, name='searchCars'),
    path('<int:pk>/CarDetails/', views.CarDetail.as_view(), name='carDetails'),
    path('register/', views.registerPage, name='register'),

    path('diesel/', views.CarsDiesel.as_view(), name='diesel'),
    path('benzina/', views.CarsBenzina.as_view(), name='benzina'),
    path('hybrid/', views.CarsHybrid.as_view(), name='hybrid'),
    path('electric/', views.CarsElectric.as_view(), name='electric'),

    path('mercedes/', views.CarsMercedes.as_view(), name='mercedes'),
    path('audi/', views.CarsAudi.as_view(), name='audi'),
    path('opel/', views.CarsOpel.as_view(), name='opel'),
    path('mazda/', views.CarsMazda.as_view(), name='mazda'),
    path('bmw/', views.CarsBMW.as_view(), name='bmw'),
    path('vw/', views.CarsVW.as_view(), name='vw'),
    path('ford/', views.CarsFord.as_view(), name='ford'),
    path('dacia/', views.CarsDacia.as_view(), name='dacia'),
    path('skoda/', views.CarsSkoda.as_view(), name='skoda'),
    path('seat/', views.CarsSeat.as_view(), name='seat'),
    path('honda/', views.CarsHonda.as_view(), name='honda'),
    path('peugeot/', views.CarsPeugeot.as_view(), name='peugeot'),

    path('motor16/', views.Cars16.as_view(), name='motor16'),
    path('motor18/', views.Cars18.as_view(), name='motor18'),
    path('motor14/', views.Cars14.as_view(), name='motor14'),
    path('motor20/', views.Cars20.as_view(), name='motor20'),
    path('motor22/', views.Cars22.as_view(), name='motor22'),
    path('motor12/', views.Cars12.as_view(), name='motor12'),

    path('automat/', views.CarsAutomata.as_view(), name='automat'),
    path('manual/', views.CarsManuala.as_view(), name='manual'),

    path('rent/', views.rentPage, name='rent'),
    path('inchiriere/', views.inchirierePage, name='inchiriere'),
    path('termeni&conditii/', views.termeniPage, name='termeni&conditii'),
    path('factura/', views.facturaPage, name='factura'),
    path('locatii/', views.locatiiPage, name='locatii'),
]