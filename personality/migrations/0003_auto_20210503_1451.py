# Generated by Django 3.1.4 on 2021-05-03 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210503_1451'),
        ('personality', '0002_auto_20210503_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personality',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.employee'),
        ),
    ]