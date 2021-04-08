# Generated by Django 3.1.4 on 2021-04-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20210408_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='favourited',
        ),
        migrations.AddField(
            model_name='application',
            name='favourited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('second round', 'second round'), ('applied', 'applied'), ('rejected', 'rejected'), ('interview', 'interview')], max_length=15),
        ),
    ]
