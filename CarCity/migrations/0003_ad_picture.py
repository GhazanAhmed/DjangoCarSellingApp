# Generated by Django 4.2.3 on 2023-08-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CarCity", "0002_ad_delete_usedcarad"),
    ]

    operations = [
        migrations.AddField(
            model_name="ad",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
