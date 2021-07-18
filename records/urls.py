from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('parts', views.PartListView.as_view(), name='parts'),
    path('customers', views.CustomerListView.as_view(), name='customers'),
    path('operations', views.OperationListView.as_view(), name='operations'),
    path('part/<int:pk>', views.PartDetailView.as_view(), name='part-detail'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('operation/<int:pk>', views.OperationDetailView.as_view(), name='operation-detail')
]
