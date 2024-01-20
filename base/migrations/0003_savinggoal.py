# Generated by Django 4.2.9 on 2024-01-19 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0002_category_transaction_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="SavingGoal",
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
                ("name", models.CharField(max_length=255)),
                ("target_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "current_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]