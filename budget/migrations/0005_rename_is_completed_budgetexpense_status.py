# Generated by Django 4.2.5 on 2023-10-11 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("budget", "0004_budgetexpense_is_completed"),
    ]

    operations = [
        migrations.RenameField(
            model_name="budgetexpense",
            old_name="is_completed",
            new_name="status",
        ),
    ]
