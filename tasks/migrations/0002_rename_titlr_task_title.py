# Generated by Django 5.1.3 on 2024-11-28 04:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="titlr",
            new_name="title",
        ),
    ]
