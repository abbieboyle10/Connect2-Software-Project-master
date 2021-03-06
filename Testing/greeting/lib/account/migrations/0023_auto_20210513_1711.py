# Generated by Django 3.1.4 on 2021-05-13 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20210513_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('interview', 'interview'), ('second round', 'second round'), ('rejected', 'rejected'), ('accepted', 'accepted'), ('applied', 'applied')], max_length=15),
        ),
        migrations.CreateModel(
            name='LTM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=200)),
                ('tag', models.CharField(blank=True, max_length=200)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.employee')),
            ],
        ),
        migrations.CreateModel(
            name='LocationTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.job')),
            ],
        ),
    ]
