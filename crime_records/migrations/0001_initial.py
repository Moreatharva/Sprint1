# Generated by Django 5.0.1 on 2025-05-11 17:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(max_length=20, unique=True)),
                ('crime_type', models.CharField(choices=[('THEFT', 'Theft'), ('ASSAULT', 'Assault'), ('BURGLARY', 'Burglary'), ('FRAUD', 'Fraud'), ('OTHER', 'Other')], max_length=20)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('date_reported', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_occurred', models.DateTimeField()),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('UNDER_INVESTIGATION', 'Under Investigation'), ('CLOSED', 'Closed')], default='OPEN', max_length=20)),
                ('suspect_name', models.CharField(blank=True, max_length=100)),
                ('victim_name', models.CharField(max_length=100)),
                ('evidence', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_reported'],
            },
        ),
    ]
