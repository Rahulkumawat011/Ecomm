# Generated by Django 3.2 on 2024-06-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=20)),
                ('open_at', models.TimeField(null=True)),
                ('close_at', models.TimeField(null=True)),
                ('description', models.TextField(max_length=100)),
                ('country', models.CharField(max_length=20, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('landmark', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
