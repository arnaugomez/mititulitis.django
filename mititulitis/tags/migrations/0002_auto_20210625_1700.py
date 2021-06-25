# Generated by Django 3.2.4 on 2021-06-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='isCertificate',
        ),
        migrations.AddField(
            model_name='tag',
            name='is_certificate',
            field=models.BooleanField(blank=True, default=False, verbose_name='This learning path involves a certificate or exam'),
        ),
    ]
