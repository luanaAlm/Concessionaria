# Generated by Django 2.2.1 on 2022-01-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
