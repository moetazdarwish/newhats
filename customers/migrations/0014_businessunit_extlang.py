# Generated by Django 4.0 on 2023-11-12 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_businessunit_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessunit',
            name='extlang',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
