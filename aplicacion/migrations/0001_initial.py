# Generated by Django 5.0.1 on 2024-02-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nutrientes', models.CharField(max_length=100)),
                ('dosis', models.CharField(max_length=100)),
                ('precauciones', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Maceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=50)),
                ('forma', models.CharField(max_length=50)),
                ('tamaño', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ambiente', models.CharField(max_length=50)),
                ('riego', models.CharField(max_length=50)),
                ('iluminacion', models.CharField(max_length=50)),
                ('tamaño', models.CharField(max_length=50)),
            ],
        ),
    ]
