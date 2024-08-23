from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='categories')

class JobAi(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='job_ai')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    description = models.TextField(blank=True, null=True)
    roles = models.JSONField(max_length=100, blank=True, null=True)
    skills = models.JSONField(max_length=100, blank=True, null=True)