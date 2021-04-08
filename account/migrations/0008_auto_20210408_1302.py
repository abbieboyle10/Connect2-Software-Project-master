# Generated by Django 3.1.4 on 2021-04-08 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210407_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='favourited',
        ),
        migrations.AddField(
            model_name='application',
            name='favourited',
            field=models.ManyToManyField(related_name='application', to='account.Employee'),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('applied', 'applied'), ('interview', 'interview'), ('rejected', 'rejected'), ('second round', 'second round')], max_length=15),
        ),
    ]