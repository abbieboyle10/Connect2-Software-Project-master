# Generated by Django 3.1.4 on 2021-05-03 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210412_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('second round', 'second round'), ('rejected', 'rejected'), ('interview', 'interview'), ('applied', 'applied')], max_length=15),
        ),
    ]
