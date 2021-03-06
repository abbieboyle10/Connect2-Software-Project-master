# Generated by Django 3.1.4 on 2021-05-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20210511_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewplan',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='interviewplan',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Confirmed', 'Confirmed'), ('Rejected', 'Rejected')], default='Open', max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('interview', 'interview'), ('rejected', 'rejected'), ('second round', 'second round'), ('applied', 'applied')], max_length=15),
        ),
    ]
