# Generated by Django 5.0 on 2024-01-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l1_support', '0002_alter_error_code_applies_to_alter_error_code_cause_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='error_code',
            name='check_list',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='error_code',
            name='place_holder',
            field=models.JSONField(null=True),
        ),
    ]