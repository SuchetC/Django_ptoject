# Generated by Django 4.1.5 on 2023-02-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fare',
            fields=[
                ('trainNum', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('OrgCity', models.CharField(max_length=250)),
                ('DesCity', models.CharField(max_length=250)),
                ('TrainFare', models.PositiveIntegerField()),
            ],
        ),
    ]