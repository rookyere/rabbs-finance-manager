# Generated by Django 4.2.5 on 2023-10-11 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budget", "0006_alter_budgetexpense_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="budgetexpense",
            name="status",
        ),
        migrations.AddField(
            model_name="budgetexpense",
            name="est_status",
            field=models.CharField(
                choices=[
                    ("budget assigned", "budget assigned"),
                    ("completed", "completed"),
                    ("Pending budget", "Pending budget"),
                ],
                default="Pending budget",
                max_length=50,
                verbose_name="Status",
            ),
        ),
    ]