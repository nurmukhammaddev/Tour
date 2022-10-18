# Generated by Django 4.1.1 on 2022-10-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=211)),
                ('avatar', models.ImageField(upload_to='person')),
                ('location', models.CharField(max_length=211)),
                ('content', models.TextField()),
            ],
        ),
    ]