# Generated by Django 4.0 on 2023-11-14 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0015_clincdays_clincdoctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClincSub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('name_lc', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.businessunit')),
            ],
        ),
        migrations.AddField(
            model_name='clincdays',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.clincsub'),
        ),
    ]
