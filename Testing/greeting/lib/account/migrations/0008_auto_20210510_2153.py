# Generated by Django 3.1.4 on 2021-05-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210503_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='person_avatar',
            field=models.ImageField(default='owls.png', upload_to='avatar_pics'),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('second round', 'second round'), ('applied', 'applied'), ('rejected', 'rejected'), ('interview', 'interview')], max_length=15),
        ),
    ]