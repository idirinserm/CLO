# Generated by Django 4.2.3 on 2023-10-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
                ('base_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_management.hotel')),
                ('services', models.ManyToManyField(to='service_management.service')),
            ],
        ),
    ]
