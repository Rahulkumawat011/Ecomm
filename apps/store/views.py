from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.store.forms import CreateStoreForm
from apps.store.models import Store


# Create your views here.

class UpdateStoreView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Store
    form_class = CreateStoreForm
    template_name = 'admin/store/form.html'
    success_message = "product updated successfully"
    success_url = reverse_lazy('admin-store-list')


class DeleteStoreView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Store

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)


class ListStoreView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/store/list.html'


class ListStoreViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Store
    columns = ['name', 'open_at', 'close_at', 'description', 'country',  'pincode', 'landmark', 'city', 'state', 'actions']
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

        if column == 'actions':
            # detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
            #     reverse('admin-category-detail', kwargs={'pk': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-store-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-store-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
            # return edit_action
        else:
            return super(ListStoreViewJson, self).render_column(row, column)


class CreateStoreView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Store
    form_class = CreateStoreForm
    template_name = 'admin/store/form.html'
    success_message = "store created successfully"
    success_url = reverse_lazy('admin-store-list')
