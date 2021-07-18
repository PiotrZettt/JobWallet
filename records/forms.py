from django.forms import ModelForm
from .models import Operation, Part, Customer

class AddOperation(ModelForm):
    class Meta:
        model = Part
        fields = ['customer', 'FGCode', 'operation', 'serial_number']