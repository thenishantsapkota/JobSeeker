# Generated by Django 4.2 on 2023-04-26 03:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicantprofile",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
