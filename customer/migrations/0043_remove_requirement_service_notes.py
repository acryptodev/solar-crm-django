# Generated by Django 3.0.5 on 2020-04-30 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0042_servicenote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirement',
            name='service_notes',
        ),
    ]
