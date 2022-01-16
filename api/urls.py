from django.urls import path
from api import views
from api.serializers import PartInstanceSerializer
from api.views import UserList, UserDetail, PartInstanceList, PartInstanceDetail, OperationList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('parts', views.PartInstanceList.as_view(), name='part-list'),
    path('parts/<str:serial_number>', views.PartInstanceDetail.as_view(), name='part-detail'),
    path('operations', views.OperationList.as_view(), name='operation-list'),
    path('add-operation', views.AddOperation.as_view(), name='add-operation'),
    path('operations/<str:operation>', views.OperationDetail.as_view(), name='operation-rud'),
]



