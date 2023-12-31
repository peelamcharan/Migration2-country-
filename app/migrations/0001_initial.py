# Generated by Django 3.2.19 on 2023-06-17 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('Capital_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Capitalname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('countryname', models.CharField(max_length=100)),
                ('capital_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.capital')),
            ],
        ),
    ]
