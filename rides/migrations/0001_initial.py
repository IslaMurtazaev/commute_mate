# Generated by Django 4.2.18 on 2025-01-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('creator_type', models.CharField(choices=[('driver', 'Driver'), ('passenger', 'Passenger')], max_length=10)),
                ('start_location', models.CharField(max_length=255)),
                ('end_location', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('new', 'New'), ('complete', 'Complete')], default='new', max_length=10)),
                ('note', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
