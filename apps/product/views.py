import csv

from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView

from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.product.forms import CreateProductForm, CreateAddProductForm, CreateAddProductOptionForm
from apps.product.models import Product, ProductAddOn, ProductAddOnOption
import csv
from .forms import CSVUploadForm
from ..category.models import Category


class UpdateProductView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'admin/product/form.html'
    success_message = "product updated successfully"
    success_url = reverse_lazy('admin-product-list')

class DeleteProductView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)


class ListProductView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/product/list.html'


class ListProductViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Product
    columns = ['category', 'product_name', 'price', 'description', 'available', 'stock', 'is_feature', 'is_popular', 'actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        # return self.model.objects.filter(Q(is_staff=False) | Q(is_superuser=False))
        return self.model.objects.all()

    def render_column(self, row, column):
        if column == 'is_ace':
            if row.is_active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'

        if column == 'actions':
            add_on_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Add on</a>'.format(
                reverse('admin-product-addon-list', kwargs={'product_id': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-product-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-product-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action + add_on_action
        else:
            return super(ListProductViewJson, self).render_column(row, column)


class CreateProductView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'admin/product/form.html'
    success_message = "product created successfully"
    success_url = reverse_lazy('admin-product-list')


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']

            if not csv_file.name.endswith('.csv'):
                form.add_error('csv_file', 'This is not a CSV file.')
                return render(request, 'admin/product/csv_upload.html', {'form': form})

        # try:
            file_data = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(file_data)
            for row in reader:
                print("row", row)
                category = row['Category']
                product_name = row['Product']
                price = row['Price']
                description = row['Description']
                available = row['Available']
                stock = row['Stock']
                is_feature = row['Feature']
                is_popular = row['Popular']

                category_obj, created = Category.objects.get_or_create(name=category)
                Product.objects.create(
                    category=category_obj,
                    product_name=product_name,
                    price=price,
                    description=description,
                    available=available,
                    stock=stock,
                    is_feature=is_feature,
                    is_popular=is_popular,

                )

            return render(request,'admin/product/list.html')

    else:
        form = CSVUploadForm()

    return render(request, 'admin/product/csv_upload.html', {'form': form})


class ListProductAddOnView(TemplateView):
    template_name = 'admin/product/addon_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListProductAddOnView, self).get_context_data(**kwargs)
        context['product_id'] = kwargs['product_id']
        return context


class CreateProductAddView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ProductAddOn
    form_class = CreateAddProductForm
    template_name = 'admin/product/form.html'
    success_message = "product_addon created successfully"
    success_url = reverse_lazy('admin-product-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_id'] = self.kwargs['product_id']
        return context

    def form_valid(self, form):
        addon_obj = form.save(commit=False)
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        addon_obj.product = product
        addon_obj.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ListProductAddOnViewJson(AdminRequiredMixin, AjayDatatableView):
    model = ProductAddOn
    columns = ['product', 'title', 'type', 'is_required','actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        print("proddjhdjdhdjhd",self.request.GET.get('product_id'))
        product_id = self.request.GET.get('product_id')
        # return self.model.objects.filter(Q(is_staff=False) | Q(is_superuser=False))
        return self.model.objects.filter(product_id=product_id)

    def render_column(self, row, column):
        if column == 'is_active':
            if row.is_active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'

        if column == 'actions':
            add_on_option_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">option</a>'.format(
                reverse('admin-product-addonoption-list', kwargs={'productaddon_id': row.pk}))

            return add_on_option_action
        else:
            return super(ListProductAddOnViewJson, self).render_column(row, column)


class ListProductAddOnOptionView(TemplateView):
    template_name = 'admin/product/addon_option_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListProductAddOnOptionView, self).get_context_data(**kwargs)
        context['productaddon_id'] = kwargs['productaddon_id']
        return context


class ListProductAddOnOptionViewJson(AjayDatatableView):
    model = ProductAddOnOption
    columns = ['addon', 'title', 'price']

    def get_initial_queryset(self):
        print("productoption",self.request.GET.get('productaddon_id'))
        addon_id = self.request.GET.get('productaddon_id')
        # return self.model.objects.filter(Q(is_staff=False) | Q(is_superuser=False))
        return self.model.objects.filter(addon_id=addon_id)


class CreateProductAddOptionView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ProductAddOnOption
    form_class = CreateAddProductOptionForm
    template_name = 'admin/product/form.html'
    success_message = "product_addonoption created successfully"
    success_url = reverse_lazy('admin-product-list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productaddon_id'] = self.kwargs['productaddon_id']
        return context

    def form_valid(self, form):
        addonoption_obj = form.save(commit=False)
        productaddon_id = self.kwargs['productaddon_id']
        productoption = get_object_or_404(ProductAddOn, id=productaddon_id)
        addonoption_obj.addon = productoption
        addonoption_obj.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)






