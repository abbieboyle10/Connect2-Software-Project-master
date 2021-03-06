# Generated by Django 3.1.4 on 2021-05-12 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20210512_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('accepted', 'accepted'), ('interview', 'interview'), ('applied', 'applied'), ('second round', 'second round')], max_length=15),
        ),
        migrations.CreateModel(
            name='TopThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.employee')),
                ('jobranking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.jobrankings')),
            ],
        ),
    ]
