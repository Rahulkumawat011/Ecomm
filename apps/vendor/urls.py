from django.urls import path

from apps.vendor.views import ListVendorView, ListVendorViewJson, CreateVendorView, UpdateVendorView, DeleteVendorView

urlpatterns = [
    path('admin/vendor/', ListVendorView.as_view(), name='admin-vendor-list'),
    path('admin/vendor/list/ajax', ListVendorViewJson.as_view(), name='admin-vendor-list-ajax'),
    path('admin/vendor/add', CreateVendorView.as_view(), name='admin-vendor-add'),
    path('admin/vendor/edit/<int:pk>', UpdateVendorView.as_view(), name='admin-vendor-edit'),
    path('admin/vendor/delete/<int:pk>', DeleteVendorView.as_view(), name='admin-vendor-delete'),

]
