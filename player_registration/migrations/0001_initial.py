# Generated by Django 4.1.1 on 2022-12-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player_Registration_Form",
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
                ("name", models.CharField(max_length=80)),
                ("phone_no", models.IntegerField()),
                ("whatsapp_no", models.IntegerField()),
                ("reference_person", models.CharField(max_length=80)),
                ("is_available", models.BooleanField()),
            ],
        ),
    ]
