# Generated by Django 3.0.5 on 2020-04-27 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0021_auto_20200427_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-created_date'], 'permissions': [('customer_list', 'Can view New Customer List page'), ('customer_view', 'Can view New Customer details'), ('deposit_list', 'Can view Deposit List page'), ('deposit_view', 'Can view Deposit details'), ('on_file_list', 'Can view On File List page'), ('on_file_view', 'Can view On File details'), ('order_list', 'Can view Order List page'), ('order_view', 'Can view Order details'), ('installation_list', 'Can view Installation List page'), ('installation_view', 'Can view Installation details'), ('account_list', 'Can view Account List page'), ('account_view', 'Can view Account details'), ('service_list', 'Can view Service List page'), ('service_view', 'Can view Service details'), ('finished_list', 'Can view Finished List page'), ('finished_view', 'Can view Finished details')]},
        ),
    ]
