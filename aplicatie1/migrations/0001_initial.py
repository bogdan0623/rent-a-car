# Generated by Django 4.0.4 on 2022-06-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('Mercedes', 'MERCEDES'), ('Audi', 'AUDI'), ('Opel', 'OPEL'), ('Mazda', 'MAZDA'), ('BMW', 'BMW'), ('Volkswagen', 'VOLKSWAGEN'), ('Ford', 'FORD'), ('Dacia', 'DACIA'), ('Skoda', 'SKODA'), ('Seat', 'SEAT'), ('Honda', 'HONDA'), ('Peugeot', 'PEUGEOT')], max_length=45)),
                ('model', models.CharField(max_length=45)),
                ('an_aparitie', models.IntegerField()),
                ('combustibil', models.CharField(choices=[('DIESEL', 'DIESEL'), ('BENZINA', 'BENZINA'), ('HYBRID', 'HYBRID'), ('ELECTRIC', 'ELECTRIC')], max_length=45)),
                ('motorizare', models.FloatField()),
                ('consum', models.FloatField()),
                ('cai_putere', models.IntegerField()),
                ('poza', models.ImageField(upload_to='cars')),
                ('pret', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]
