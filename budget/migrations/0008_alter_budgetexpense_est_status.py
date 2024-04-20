# Generated by Django 4.2.5 on 2023-10-11 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budget", "0007_remove_budgetexpense_status_budgetexpense_est_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="budgetexpense",
            name="est_status",
            field=models.CharField(
                choices=[
                    ("Budget assigned", "Budget assigned"),
                    ("Completed", "Completed"),
                    ("Pending budget", "Pending budget"),
                ],
                default="Pending budget",
                max_length=50,
                verbose_name="Status",
            ),
        ),
    ]
