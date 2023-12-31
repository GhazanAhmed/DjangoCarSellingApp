# Generated by Django 4.2.3 on 2023-08-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UsedCarAd",
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
                ("brand", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("year", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("contact_info", models.CharField(max_length=200)),
                ("date_published", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
