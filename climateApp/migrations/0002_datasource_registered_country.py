# Generated by Django 4.1.6 on 2023-02-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("climateApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="datasource",
            name="registered_country",
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]