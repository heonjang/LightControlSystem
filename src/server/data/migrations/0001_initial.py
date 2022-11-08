# Generated by Django 4.1.2 on 2022-10-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LightIntensityPoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sensor_name", models.CharField(db_index=True, max_length=20)),
                ("time", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("value", models.FloatField()),
            ],
        ),
    ]