# Generated by Django 4.2.5 on 2023-09-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rater",
            name="review",
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
