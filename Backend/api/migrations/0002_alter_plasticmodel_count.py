# Generated by Django 4.2.6 on 2023-11-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plasticmodel",
            name="count",
            field=models.IntegerField(default=0),
        ),
    ]