from django.shortcuts import render
from .models import Customer, Part, Operation
from django.views import generic

# Create your views here.


def index(request):

    num_parts = Part.objects.all().count()
    num_customers = Customer.objects.all().count()

    context = {
        'num_part': num_parts,
        'num_customers': num_customers,
    }
    return render(request, 'index.html', context)


class PartListView(generic.ListView):

    model = Part


class PartDetailView(generic.DetailView):

    model = Part


class CustomerListView(generic.ListView):

    model = Customer


class CustomerDetailView(generic.DetailView):

    model = Customer


class OperationDetailView(generic.DetailView):

    model = Operation


class OperationListView(generic.ListView):

    model = Operation
