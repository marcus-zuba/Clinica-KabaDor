# Generated by Django 2.1.5 on 2022-02-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0002_auto_20220210_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='crm',
            field=models.IntegerField(unique=True),
        ),
    ]
