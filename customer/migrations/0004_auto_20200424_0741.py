# Generated by Django 3.0.5 on 2020-04-23 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20200424_0730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-created_date']},
        ),
    ]
