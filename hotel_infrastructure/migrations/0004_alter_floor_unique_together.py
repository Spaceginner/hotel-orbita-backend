# Generated by Django 5.2.4 on 2025-07-19 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "hotel_infrastructure",
            "0003_building_address_building_name_alter_room_number_and_more",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="floor",
            unique_together={("building", "level")},
        ),
    ]
