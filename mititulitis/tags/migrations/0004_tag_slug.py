# Generated by Django 3.2.4 on 2021-06-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20210625_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]
