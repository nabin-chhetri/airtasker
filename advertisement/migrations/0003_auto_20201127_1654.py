# Generated by Django 3.1.3 on 2020-11-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_auto_20201127_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='ads_status',
            field=models.CharField(choices=[('', 'Select ads status'), ('Inactive', 'Inactive'), ('Under-Review', 'Under-Review'), ('Active', 'Active')], default='Inactivec', max_length=20),
        ),
    ]
