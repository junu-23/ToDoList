# Generated by Django 4.0.3 on 2024-09-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dodo', '0002_alter_doit_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='doit',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
