# Generated by Django 5.0.6 on 2024-06-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0005_remove_address_city_remove_address_postalcode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='id',
        ),
        migrations.AddField(
            model_name='address',
            name='address_code',
            field=models.CharField(default=0, max_length=255, primary_key=True, serialize=False),
        ),
    ]
