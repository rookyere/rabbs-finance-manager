# Generated by Django 4.2.5 on 2023-10-07 16:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("expense", "0002_alter_expensetype_options_alter_expense_exp_source"),
        ("budget", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="budgetexpense",
            name="ext_date_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="budgetexpense",
            name="est_expense_source",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="expense.expensetype",
                verbose_name="Expense Category",
            ),
        ),
    ]
