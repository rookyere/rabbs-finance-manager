# Generated by Django 4.2.5 on 2023-10-07 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("budget", "0002_budgetexpense_ext_date_time_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="budgetexpense",
            old_name="ext_date_time",
            new_name="est_date_time",
        ),
    ]
