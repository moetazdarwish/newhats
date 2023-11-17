# Generated by Django 4.0 on 2023-11-14 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0014_alter_whatsmsgconve_msg'),
        ('customers', '0017_remove_clincdays_section'),
        ('cart', '0003_cartsimple'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.businessunit')),
                ('clinc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.clincdoctor')),
                ('conver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='whatsapp.whatsmsg')),
                ('cust', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customerprofile')),
            ],
        ),
    ]