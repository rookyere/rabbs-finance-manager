# Generated by Django 4.2.5 on 2023-10-07 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("expense", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="expensetype",
            options={"ordering": ["exp_source"]},
        ),
        migrations.AlterField(
            model_name="expense",
            name="exp_source",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="expense.expensetype",
                verbose_name="Expense Category",
            ),
        ),
    ]
