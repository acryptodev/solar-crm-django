# Generated by Django 3.0.5 on 2020-05-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0046_delete_outlooktokencache'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='create_notification',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
