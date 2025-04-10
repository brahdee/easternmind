# Generated by Django 5.1.1 on 2024-09-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_image_format"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="format",
            field=models.CharField(
                choices=[("F", "Film"), ("O", "Other")], default=1, max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
