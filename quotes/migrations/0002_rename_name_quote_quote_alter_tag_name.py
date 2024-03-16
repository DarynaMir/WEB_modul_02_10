# Generated by Django 5.0.3 on 2024-03-16 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quote",
            old_name="name",
            new_name="quote",
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
