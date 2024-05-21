# Generated by Django 4.2.13 on 2024-05-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Track",
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
                ("title", models.CharField(max_length=100)),
                ("artist", models.CharField(max_length=100)),
                ("file", models.FileField(upload_to="tracks/")),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
