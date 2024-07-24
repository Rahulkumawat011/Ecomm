# Generated by Django 3.2 on 2024-06-24 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_favoriteproduct_productaddon_productaddonoption'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addon_data', models.CharField(blank=True, max_length=25, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItemAddOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartitem')),
                ('product_addon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productaddon')),
            ],
        ),
        migrations.CreateModel(
            name='CartItemAddOnOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('Product_addon_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productaddonoption')),
                ('cart_item_addon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartitemaddon')),
            ],
        ),
    ]
