# Generated by Django 2.2.1 on 2022-01-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220105_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='carros',
            name='categoria',
            field=models.CharField(choices=[('Destaques', 'Destaques'), ('Seminovos', 'Seminovos')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
