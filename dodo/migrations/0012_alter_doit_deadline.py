# Generated by Django 4.0.3 on 2024-09-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dodo', '0011_alter_doit_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doit',
            name='deadline',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
