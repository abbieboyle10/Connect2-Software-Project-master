# Generated by Django 3.1.4 on 2021-04-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210406_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('applied', 'applied'), ('interview', 'interview'), ('second round', 'second round'), ('rejected', 'rejected')], max_length=15),
        ),
    ]
