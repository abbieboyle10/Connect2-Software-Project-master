# Generated by Django 3.1.4 on 2021-05-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_auto_20210513_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationtag',
            name='tag',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('interview', 'interview'), ('second round', 'second round'), ('accepted', 'accepted'), ('applied', 'applied')], max_length=15),
        ),
    ]
