# Generated by Django 5.0.6 on 2024-06-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clients",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Nom", models.CharField(max_length=255)),
                ("Prenom", models.CharField(max_length=255)),
            ],
        ),
    ]
