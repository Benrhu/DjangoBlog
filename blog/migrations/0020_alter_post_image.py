# Generated by Django 4.1.7 on 2023-02-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0019_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="static/images"),
        ),
    ]
