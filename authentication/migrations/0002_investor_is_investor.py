# Generated by Django 4.1.7 on 2023-02-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="investor",
            name="is_investor",
            field=models.BooleanField(default=False),
        ),
    ]