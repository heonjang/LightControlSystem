# Generated by Django 4.1.2 on 2022-10-16 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="LightIntensityPoint",
            new_name="LightIntensity",
        ),
        migrations.RenameField(
            model_name="lightintensity",
            old_name="sensor_name",
            new_name="sensor",
        ),
    ]
