# Generated by Django 4.0 on 2023-11-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0013_whatsmsgconve_reptxt_whatsmsgreply_reptxt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsmsgconve',
            name='msg',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
