# Generated by Django 4.0.3 on 2024-09-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dodo', '0006_alter_doit_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='doit',
            name='detail',
            field=models.TextField(blank=True, default=''),
        ),
    ]
