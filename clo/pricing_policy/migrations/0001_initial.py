# Generated by Django 4.2.3 on 2023-10-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=10)),
                ('is_weekend', models.BooleanField()),
                ('is_single_occupancy', models.BooleanField()),
                ('price_adjustment', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_management.hotel')),
            ],
        ),
    ]
