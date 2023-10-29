from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView

# Create your views here.
from aplicatie1.forms import CreateUserForm
from aplicatie1.models import Car

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'aplicatie1/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'aplicatie1/login.html', context)

def rentPage(request):
    context = {}
    return render(request, 'aplicatie1/rent.html', context)

def inchirierePage(request):
    context = {}
    return render(request, 'aplicatie1/inchiriere.html', context)

def termeniPage(request):
    context = {}
    return render(request, 'aplicatie1/termeni.html', context)

def facturaPage(request):
    context = {}
    return render(request, 'aplicatie1/factura.html', context)

def locatiiPage(request):
    context = {}
    return render(request, 'aplicatie1/locatii.html', context)

class CarsView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'


    def get_context_data(self, *args, **kargs):
        data = super(CarsView, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(active=1)
        return data

class CreateCarsView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['marca', 'model', 'an_aparitie', 'combustibil', 'motorizare', 'consum','cutie', 'cai_putere', 'pret', 'location', 'poza']
    template_name = 'aplicatie1/cars_form.html'


    def get_success_url(self):
        return reverse('carApp:lista_masini')



class UpdateCarsView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['marca', 'model', 'an_aparitie', 'combustibil', 'motorizare', 'consum','cutie', 'cai_putere', 'pret','location', 'poza']
    template_name = 'aplicatie1/cars_form.html'

    def get_success_url(self):
        return reverse('carApp:lista_masini')

@login_required
def search_cars(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cars = Car.objects.filter(marca__contains=searched)
        return render(request, 'aplicatie1/search_cars.html', {'searched': searched, 'cars': cars})
    else:
        return render(request, 'aplicatie1/search_cars.html', {})

@login_required
def delete_cars(request, pk):
    Car.objects.filter(id=pk).update(active=0)
    return redirect('carApp:lista_masini')

@login_required
def activate_cars(request, pk):
    Car.objects.filter(id=pk).update(active=1)
    return redirect('carApp:lista_masini')


class CarsInactiveView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'
    paginate_by = 8
    queryset = model.objects.filter(active=0)
    context_object_name = 'cars'

    def get_context_data(self, *args, **kargs):
        data = super(CarsInactiveView, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(active=0)
        return data

class  CarDetail(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'aplicatie1/car_detail.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarDetail, self).get_context_data(*args, **kargs)
        data['carsL'] = self.model.objects.filter(active=1)
        return data

class CarsDiesel(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsDiesel, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(combustibil='DIESEL')
        return data

class CarsBenzina(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsBenzina, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(combustibil='BENZINA')
        return data


class CarsHybrid(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsHybrid, self).get_context_data(*args, **kargs)
        data['carsL'] = self.model.objects.filter(combustibil='HYBRID')
        return data


class CarsElectric(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsElectric, self).get_context_data(*args, **kargs)
        data['carsL'] = self.model.objects.filter(combustibil='ELECTRIC')
        return data


class CarsMercedes(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsMercedes, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Mercedes')
        return data

class CarsAudi(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsAudi, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Audi')
        return data

class CarsOpel(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsOpel, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Opel')
        return data

class CarsMazda(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsMazda, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Mazda')
        return data

class CarsBMW(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsBMW, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='BMW')
        return data

class CarsVW(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsVW, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Volkswagen')
        return data

class CarsFord(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsFord, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Ford')
        return data

class CarsDacia(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsDacia, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Dacia')
        return data

class CarsSkoda(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsSkoda, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Skoda')
        return data

class CarsSeat(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsSeat, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Seat')
        return data

class CarsHonda(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsHonda, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Honda')
        return data

class CarsPeugeot(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsPeugeot, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(marca='Peugeot')
        return data

class Cars16(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(Cars16, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(motorizare=1.6)
        return data

class Cars18(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(Cars18, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(motorizare=1.8)
        return data

class Cars14(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(Cars14, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(motorizare=1.4)
        return data

class Cars20(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(Cars20, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(motorizare=2.0)
        return data

class Cars22(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(Cars22, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(motorizare=2.2)
        return data

class Cars12(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(Cars12, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(motorizare=1.2)
        return data

class CarsAutomata(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsAutomata, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(cutie='AUTOMATA')
        return data

class CarsManuala(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'aplicatie1/cars_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CarsManuala, self).get_context_data( *args, **kargs)
        data['carsL'] = self.model.objects.filter(cutie='MANUALA')
        return data