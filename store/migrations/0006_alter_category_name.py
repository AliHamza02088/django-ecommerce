# Generated by Django 5.1.4 on 2024-12-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_alter_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                choices=[
                    ("Mobile", "Mobile"),
                    ("Tablet", "Tablet"),
                    ("Laptop", "Laptop"),
                    ("Watch", "Watch"),
                    ("Gadget", "Gadget"),
                    ("Speaker", "Speaker"),
                    ("Accessories", "Accessories"),
                    ("Computer", "Computer"),
                ],
                max_length=255,
            ),
        ),
    ]
