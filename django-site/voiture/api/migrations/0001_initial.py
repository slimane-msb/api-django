# Generated by Django 4.2.15 on 2024-09-04 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couleur', models.CharField(max_length=30)),
                ('immatriculation', models.CharField(max_length=9)),
                ('marque', models.CharField(max_length=30)),
                ('modele', models.CharField(max_length=30)),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.garage')),
            ],
        ),
        migrations.CreateModel(
            name='Cle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat_pret', models.BooleanField()),
                ('date_pret', models.DateField()),
                ('date_rendu', models.DateField()),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voiture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.voiture')),
            ],
        ),
    ]