# Generated by Django 4.0 on 2023-11-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invcategory',
            name='cat_lc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='Description_lc',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_lc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
