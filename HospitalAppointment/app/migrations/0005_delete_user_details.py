# Generated by Django 5.1.2 on 2024-10-09 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_user_details"),
    ]

    operations = [
        migrations.DeleteModel(
            name="user_details",
        ),
    ]
