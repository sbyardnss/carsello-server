# Generated by Django 4.2.3 on 2023-07-28 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsello_api', '0002_remove_artwork_date_artwork_year_alter_artwork_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
