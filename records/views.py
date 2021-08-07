from django.shortcuts import render, redirect
from .models import Customer, Part, PartInstance, Operation, Wallet
from django.views import generic
from .forms import AddOperationModelForm, CreateJobWalletModelForm, SearchForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def index(request):

    num_parts = Part.objects.all().count()
    num_customers = Customer.objects.all().count()

    context = {
        'num_part': num_parts,
        'num_customers': num_customers,
    }
    print(num_customers, num_parts)
    return render(request, 'index.html', context)


def add_operation(request, pk):
    form = AddOperationModelForm()
    user = request.user
    if request.method == 'POST':
        print('received post request')
        form = AddOperationModelForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            Operation.objects.create(
                processed_part=PartInstance.objects.get(pk=pk),
                operation_name=form.cleaned_data['operation_name'],
                date_signed=Operation.date_signed,
                comments=form.cleaned_data['comments'],
                operator=user,
                operation_status=form.cleaned_data['operation_status']
            )

        return redirect('index')

    context = {
        'form': form,
        'user': user
    }
    return render(request, 'add_operation.html', context)


def create_job_wallet(request):
    form = CreateJobWalletModelForm()

    if request.method == 'POST':
        print('received post request')
        form = CreateJobWalletModelForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            new_wallet = Wallet.objects.create(
                order_number=form.cleaned_data['order_number'],
                order_quantity=form.cleaned_data['order_quantity'],
                customer_name=form.cleaned_data['customer_name'],
                part_FG=form.cleaned_data['part_FG'],
                part_id=form.cleaned_data['part_id'],
                pack_number=form.cleaned_data['pack_number'],
                traceability_required=form.cleaned_data['traceability_required']
            )
            parts_list = []
            order_quantity = form.cleaned_data['order_quantity']
            order_number = form.cleaned_data['order_number']
            for i in range(1, order_quantity + 1):
                single_number = str(i) + '-' + str(order_number)
                parts_list.append(single_number)
            for number in parts_list:
                PartInstance.objects.create(job_wallet=new_wallet,
                                            part_origin=form.cleaned_data['part_FG'], serial_number=number)
            print(parts_list)

        return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'create_job_wallet.html', context)


def search(request):

    parts = None
    if request.method == 'POST':
        print('received get request')
        searched = request.POST['searched']
        parts = PartInstance.objects.filter(serial_number__contains=searched)
        # .filter(part_origin__customer=form.cleaned_data['customer']).filter(part_origin__FG_code__icontains=form.cleaned_data['part_FG'])
        print(parts)
    context = {

        'parts': parts
    }

    return render(request, 'search_results.html', context)


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

class SearchResultsView(generic.ListView):
    model = Part
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Part.objects.filter(name__icontains=query)

        return object_list


class OperationListView(generic.ListView):

    model = Operation

class PartInstanceListView(generic.ListView):

    model = PartInstance


class PartInstanceDetailView(generic.DetailView):

    model = PartInstance


class WalletListView(generic.ListView):

    model = Wallet


class WalletDetailView(generic.DetailView):

    model = Wallet


