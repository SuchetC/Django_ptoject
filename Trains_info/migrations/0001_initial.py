# Generated by Django 4.1.5 on 2023-02-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='train_details',
            fields=[
                ('train_num', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=260, unique=True)),
                ('origin_city', models.CharField(max_length=260)),
                ('destination_city', models.CharField(max_length=270)),
                ('departure_time', models.TimeField()),
                ('arival_time', models.TimeField()),
            ],
        ),
    ]
