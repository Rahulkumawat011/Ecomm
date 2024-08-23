from django.urls import path

from apps.healthcare import views
from apps.healthcare.views import CreateDepartment, CreateCategory, HealthTemplate, XlsUploadView

urlpatterns = [
    path('test/healthcare/', views.TestHealthCare, name='test-healthcare'),
    path('department/create/', CreateDepartment.as_view(), name='department-create'),
    path('category/create/', CreateCategory.as_view(), name='category-create'),
    path('health/template/', HealthTemplate.as_view(), name='health-template-list'),
    path('upload/xlsfile/', XlsUploadView.as_view(), name='upload-xls')
]