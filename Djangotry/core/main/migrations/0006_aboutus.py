# Generated by Django 4.2.4 on 2023-08-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_ourgallery"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutUs",
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
                ("content1", models.TextField(verbose_name="First Content")),
                ("content2", models.TextField(verbose_name="Third Content")),
            ],
            options={
                "verbose_name": "About Us",
                "verbose_name_plural": "About Us",
            },
        ),
    ]
