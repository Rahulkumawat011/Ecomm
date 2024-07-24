from django.urls import path

from apps.category.views import ListCategoryView, ListCategoryViewJson, CreateCategoryView, UpdateCategoryView, \
    DeleteCategoryView

urlpatterns = [
    path('admin/category/', ListCategoryView.as_view(), name='admin-category-list'),
    path('admin/category/list/ajax', ListCategoryViewJson.as_view(), name='admin-category-list-ajax'),
    path('admin/Category/add', CreateCategoryView.as_view(), name='admin-category-add'),
    path('admin/Category/edit/<int:pk>', UpdateCategoryView.as_view(), name='admin-Category-edit'),
    path('admin/category/delete/<int:pk>', DeleteCategoryView.as_view(), name='admin-category-delete'),

]