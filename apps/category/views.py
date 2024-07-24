from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView

from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.category.forms import CreateCategoryForm
from apps.category.models import Category


class UpdateCategoryView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'admin/category/form.html'
    success_message = "Category updated successfully"
    success_url = reverse_lazy('admin-category-list')


class DeleteCategoryView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Category

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)


class ListCategoryView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/category/list.html'


class ListCategoryViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Category
    columns = ['name', 'type', 'actions']
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
                reverse('admin-Category-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-category-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
            # return edit_action
        else:
            return super(ListCategoryViewJson, self).render_column(row, column)


class CreateCategoryView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'admin/category/form.html'
    success_message = "category created successfully"
    success_url = reverse_lazy('admin-category-list')


