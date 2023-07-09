# Generated by Django 4.2.3 on 2023-07-09 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('image', models.URLField(null=True)),
                ('link', models.URLField(null=True)),
                ('details', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
    ]
