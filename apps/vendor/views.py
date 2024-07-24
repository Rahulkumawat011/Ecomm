from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.store.forms import CreateStoreForm
from apps.store.models import Store
from apps.vendor.forms import CreateVendorForm
from apps.vendor.models import Vendor


# Create your views here.

class UpdateVendorView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Vendor
    form_class = CreateVendorForm
    template_name = 'admin/vendor/form.html'
    success_message = "product updated successfully"
    success_url = reverse_lazy('admin-vendor-list')


class DeleteVendorView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Vendor

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)


class ListVendorView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/vendor/list.html'


class ListVendorViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Vendor
    columns = ['user', 'name', 'address', 'open_at', 'close_at', 'image', 'lat', 'long', 'actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        # return self.model.objects.filter(Q(is_staff=False) | Q(is_superuser=False))
        return self.model.objects.all()

    def render_column(self, row, column):
        if column == 'is_active':
            if row.is_active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'
        if column == 'image':
            return f'<img src="{row.image.url}" alt="Girl in a jacket" width="100px" >'

        if column == 'actions':
            # detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
            #     reverse('admin-category-detail', kwargs={'pk': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-vendor-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-vendor-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
            # return edit_action
        else:
            return super(ListVendorViewJson, self).render_column(row, column)


class CreateVendorView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Vendor
    form_class = CreateVendorForm
    template_name = 'admin/vendor/form.html'
    success_message = "vendor created successfully"
    success_url = reverse_lazy('admin-vendor-list')
