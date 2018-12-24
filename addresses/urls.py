from django.urls import path

from . import views

urlpatterns = [
    path('addresses/', views.AddressListView.as_view(), name='address-list'),
    path('addresses/(?P<pk>[0-9]+)', views.AddressDetailView.as_view(), name='address-detail')
]