from django.shortcuts import render

# import all your models
from .models import (
    Salesperson,
    Mechanic,
    Customer,
    Car,
    SalesInvoice,
    Service,
    ServiceTicket,
    ServiceMechanic,
    Parts,
    PartsUsed
)


def home(request):
    return render(request, "polls/home.html", {
        "salespeople": Salesperson.objects.all(),
        "mechanics": Mechanic.objects.all(),
        "customers": Customer.objects.all(),
        "cars": Car.objects.all(),
        "invoices": SalesInvoice.objects.all(),
        "services": Service.objects.all(),
        "tickets": ServiceTicket.objects.all(),
        "servicemechanics": ServiceMechanic.objects.all(),
        "parts": Parts.objects.all(),
        "partsused": PartsUsed.objects.all(),
    })