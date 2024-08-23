import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from apps.healthcare.forms import DepartmentForm, CategorytForm, XlsUploadForm
from apps.healthcare.models import Department, Category, JobAi


# Create your views here.

def TestHealthCare(request):
    return HttpResponse('Test-HealthCare')


class CreateDepartment(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'healthcare/form.html'
    success_url = reverse_lazy('test-healthcare')


class CreateCategory(CreateView):
    model = Category
    form_class = CategorytForm
    template_name = 'item/form.html'
    success_url = reverse_lazy('health-template-list')


class XlsUploadView(FormView):
    template_name = 'healthcare/uploadXls.html'
    form_class = XlsUploadForm
    success_url = reverse_lazy('health-template-list')

    def form_valid(self, form):
        xls_file = form.cleaned_data['xls_file']
        df = pd.read_excel(xls_file)

        # Print the headers of the Excel file
        print("Excel file headers:", df.columns.tolist())

        for index, row in df.iterrows():
            # Ensure there is no ambiguity in Department and Category creation
            department, created = Department.objects.get_or_create(
                name=row.get('Department', '')
            )

            # Use a unique description to distinguish categories within the same department
            category, created = Category.objects.get_or_create(
                name=row.get('Category', ''),
                description=row.get('Description', ''),
                department=department
            )

            # Create the JobAi
            JobAi.objects.create(
                department=department,
                category=category,
                description=row.get('Job Description', ''),
                roles=row.get('Roles', {}),
                skills=row.get('Skills', {})
            )

        return super().form_valid(form)


class HealthTemplate(TemplateView):
    template_name = 'healthcare/list.html'