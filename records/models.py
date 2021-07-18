from django.db import models
from .constants import PART_DESCRIPTION, OPERATIONS
from django.contrib.auth.admin import User
from django.urls import reverse

# Create your models here.


class Customer(models.Model):
    CUSTOMERS = (
        ('McLaren', 'McLaren'),
        ('Ferrari', 'Ferrari'),
        ('Morgan', 'Morgan'),
        ('Maserati', 'Maserati'),
    )
    customer = models.CharField(max_length=120, choices=CUSTOMERS, default='Customer')

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('customer-detail', args=[str(self.id)])

    def __str__(self):
        return self.customer


class Part(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    FGcode = models.CharField(max_length=10)
    operation = models.ManyToManyField('Operation',
                                       help_text='Select an operation for this part',)

    # description = models.CharField(max_length=120, choices=PART_DESCRIPTION)
    serial_number = models.CharField(max_length=12)

    # def operations_list(self):
    #     return self.operation.all()

    def description(self):
        description_text = [fg[0] for fg in PART_DESCRIPTION if fg[1] == str(self.FGcode)]
        return description_text[0]

    def get_operations(self):
        operations = self.operation.all()
        return operations

    def get_operation_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('operation-detail', args=[str(self.operation.id)])

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('part-detail', args=[str(self.id)])

    def __str__(self):
        return self.serial_number


class Operation(models.Model):
    operation_name = models.CharField(max_length=120, choices=OPERATIONS)
    date_signed = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(null=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    STATUS = (('Passed', 'P'), ('Scrapped', 'S'), ('Quarantined', 'Q'))
    operation_status = models.CharField(max_length=120, choices=STATUS, default='What is the part status?')

    class Meta:
        ordering = ['operation_name']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('operation-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.operation_name
