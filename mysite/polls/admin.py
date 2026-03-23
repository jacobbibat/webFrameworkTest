from django.contrib import admin
from .models import Salesperson, Mechanic, Customer, Car, SalesInvoice, Service, ServiceTicket, ServiceMechanic, Parts, PartsUsed

admin.site.register(Salesperson)
admin.site.register(Mechanic)
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(SalesInvoice)
admin.site.register(Service)
admin.site.register(ServiceTicket)
admin.site.register(ServiceMechanic)
admin.site.register(Parts)
admin.site.register(PartsUsed)