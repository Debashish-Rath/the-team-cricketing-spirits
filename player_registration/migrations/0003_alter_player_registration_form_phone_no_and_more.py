# Generated by Django 4.1.1 on 2022-12-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player_registration", "0002_player_registration_form_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player_registration_form",
            name="phone_no",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="player_registration_form",
            name="whatsapp_no",
            field=models.BigIntegerField(),
        ),
    ]