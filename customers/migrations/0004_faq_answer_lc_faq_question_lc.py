# Generated by Django 4.0 on 2023-11-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_businessunit_support_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_lc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_lc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
