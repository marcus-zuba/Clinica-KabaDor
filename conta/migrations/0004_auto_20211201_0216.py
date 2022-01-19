# Generated by Django 2.1.5 on 2021-12-01 02:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0003_auto_20211130_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='telefone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{1,14}$')]),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999)]),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(max_length=10, null=True),
        ),
    ]