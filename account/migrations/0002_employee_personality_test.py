# Generated by Django 3.1.4 on 2021-03-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='personality_test',
            field=models.BooleanField(default=False),
        ),
    ]