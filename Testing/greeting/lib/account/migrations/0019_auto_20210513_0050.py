# Generated by Django 3.1.4 on 2021-05-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20210513_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedthing',
            name='sort',
            field=models.CharField(choices=[('Tag', 'Tag'), ('Skill', 'Skill')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('interview', 'interview'), ('applied', 'applied'), ('rejected', 'rejected'), ('accepted', 'accepted'), ('second round', 'second round')], max_length=15),
        ),
    ]
