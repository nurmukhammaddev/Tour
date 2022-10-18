# Generated by Django 4.1.2 on 2022-10-15 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_travel_price'),
        ('hotels', '0010_alter_hotel_stars'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.travel')),
            ],
        ),
    ]