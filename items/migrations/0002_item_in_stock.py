# Generated by Django 5.0.2 on 2024-02-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="in_stock",
            field=models.IntegerField(default=0),
        ),
    ]