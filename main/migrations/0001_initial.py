# Generated by Django 5.0.1 on 2024-05-04 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('country', models.CharField(max_length=75, verbose_name='Страна')),
                ('city', models.CharField(max_length=75, verbose_name='Город')),
                ('street', models.CharField(max_length=75, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=100, verbose_name='Номер дома')),
                ('level', models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], verbose_name='Звено сети')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('country', models.CharField(max_length=75, verbose_name='Страна')),
                ('city', models.CharField(max_length=75, verbose_name='Город')),
                ('street', models.CharField(max_length=75, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=100, verbose_name='Номер дома')),
                ('arrears', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Задолженность')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('date_release', models.DateField(verbose_name='Дата выхода')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.network', verbose_name='Звено сети')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.AddField(
            model_name='network',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.provider', verbose_name='Поставщик'),
        ),
    ]
