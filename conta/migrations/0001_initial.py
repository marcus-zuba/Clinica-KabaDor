# Generated by Django 2.1.5 on 2022-02-10 06:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDeEnderecos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('logradouro', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_contrato', models.DateField()),
                ('salario', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(max_length=50)),
                ('crm', models.IntegerField()),
                ('funcionario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='conta.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField()),
                ('altura', models.FloatField()),
                ('tipo_sanguineo', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{1,14}$')])),
                ('cep', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('logradouro', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pessoa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='pessoa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='conta.Pessoa'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='pessoa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to='conta.Pessoa'),
        ),
    ]
