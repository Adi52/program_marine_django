# Generated by Django 3.0.4 on 2020-03-27 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_place', models.CharField(max_length=5)),
                ('occupied_to', models.DateTimeField(blank=True, null=True, verbose_name='Occupied to')),
            ],
        ),
        migrations.CreateModel(
            name='EntryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name_yacht', models.CharField(max_length=30, verbose_name='Nazwa jachtu')),
                ('registration_number', models.CharField(max_length=30, verbose_name='Numer rejestracyjny')),
                ('home_port', models.CharField(max_length=30, verbose_name='Port macierzysty')),
                ('yacht_length', models.FloatField(verbose_name='Długość jachtu')),
                ('yacht_width', models.FloatField(verbose_name='Szerokość jachtu')),
                ('yacht_type', models.CharField(choices=[('żaglowy', 'ŻAGLOWY'), ('motorowy', 'MOTOROWY')], default='typ', max_length=20, verbose_name='Typ jachtu')),
                ('owner_details_name', models.CharField(max_length=30, verbose_name='Imie i nazwisko właściciela jednostki')),
                ('owner_details_address', models.CharField(max_length=100, verbose_name='Adres właściciela jednostki')),
                ('commissioning_body_name', models.CharField(max_length=100, verbose_name='Podmiot zlecający umowę')),
                ('commissioning_body_address', models.CharField(max_length=100, verbose_name='Adres')),
                ('commissioning_body_tel', models.CharField(max_length=30, verbose_name='Numer telefonu')),
                ('commissioning_body_email', models.EmailField(max_length=30, verbose_name='E-mail')),
                ('commissioning_body_nip', models.CharField(max_length=30, verbose_name='NIP')),
                ('parking_period_from', models.DateField(null=True, verbose_name='Postój od')),
                ('parking_period_to', models.DateField(null=True, verbose_name='Postój do')),
                ('correspondence_address', models.CharField(blank=True, default='Wpisz jeżeli różni się od adresu wyżej', max_length=100, verbose_name='Adres do korespondencji')),
                ('chip_card', models.BooleanField(default=False, verbose_name='Karta chipowa')),
                ('parking_place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='marine.ParkingPlace', verbose_name='Miejsce postoju')),
            ],
        ),
    ]
