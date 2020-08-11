# Generated by Django 3.0.5 on 2020-04-23 04:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('agm', models.IntegerField(blank=True, null=True)),
                ('date_signed', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric characters are allowed.')])),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElectricPower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Installer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SalesPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Storey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('agm', models.IntegerField()),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_address', models.CharField(max_length=200)),
                ('customer_email', models.EmailField(max_length=200)),
                ('customer_phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric characters are allowed.')])),
                ('installation_date', models.DateField()),
                ('notes', models.CharField(max_length=500)),
                ('installer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Installer')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kw', models.IntegerField(null=True)),
                ('panel', models.IntegerField(null=True)),
                ('inverter', models.IntegerField(null=True)),
                ('installation_notes', models.CharField(max_length=500, null=True)),
                ('extra_amount', models.IntegerField(null=True)),
                ('total_price', models.IntegerField(null=True)),
                ('deposit', models.IntegerField(null=True)),
                ('last_amount', models.IntegerField(null=True)),
                ('status', models.CharField(default='CREATED', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('electric_power', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.ElectricPower')),
                ('foor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.FoorType')),
                ('storey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Storey')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='leads_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Lead'),
        ),
        migrations.AddField(
            model_name='customer',
            name='sales_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.SalesPerson'),
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric characters are allowed.')])),
                ('expires', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
