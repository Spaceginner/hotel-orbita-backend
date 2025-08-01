# Generated by Django 5.2.4 on 2025-07-18 22:08

import django.core.validators
import django.db.models.deletion
import hotel_clients.models
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hotel_finances", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientStatus",
            fields=[
                (
                    "code",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IndividualNationality",
            fields=[
                (
                    "code",
                    models.CharField(
                        max_length=3,
                        primary_key=True,
                        serialize=False,
                        validators=[django.core.validators.MinLengthValidator(3)],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrganisationClient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="IndividualClient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("patronymic", models.CharField(blank=True, max_length=50)),
                ("birthday", models.DateField()),
                ("passport_number", models.CharField()),
                ("passport_date", models.DateField()),
                ("passport_issuer", models.CharField()),
                (
                    "nationality",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="clients",
                        related_query_name="client",
                        to="hotel_clients.individualnationality",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PassportImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "page",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=hotel_clients.models.PassportImage._get_image_path
                    ),
                ),
                (
                    "individual",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="passport_images",
                        related_query_name="passport_image",
                        to="hotel_clients.individualclient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("taxpayer_number", models.CharField(max_length=20, unique=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                ("email", models.EmailField(max_length=254, null=True, unique=True)),
                ("preferences", models.TextField(max_length=3000)),
                (
                    "discount",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="hotel_finances.price",
                    ),
                ),
                (
                    "individual",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client",
                        to="hotel_clients.individualclient",
                    ),
                ),
                (
                    "organisation",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client",
                        to="hotel_clients.organisationclient",
                    ),
                ),
            ],
            options={
                "permissions": [("set_discount", "Allow to edit client's discount")],
                "constraints": [
                    models.CheckConstraint(
                        condition=models.Q(
                            ("individual__isnull", False),
                            ("organisation__isnull", False),
                            _connector="XOR",
                        ),
                        name="individual_or_org",
                    )
                ],
            },
        ),
    ]
