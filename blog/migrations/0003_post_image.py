# Generated by Django 4.1.7 on 2023-02-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_body_post_intro_post_slug_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='https://#', upload_to=''),
            preserve_default=False,
        ),
    ]