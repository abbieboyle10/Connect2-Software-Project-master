# Generated by Django 3.1.4 on 2021-05-12 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20210512_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('applied', 'applied'), ('interview', 'interview'), ('rejected', 'rejected'), ('second round', 'second round')], max_length=15),
        ),
        migrations.CreateModel(
            name='PersonTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('category', models.CharField(choices=[('Business', 'Business'), ('IT', 'IT'), ('Retail', 'Retail')], default='Business', max_length=200)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.employee')),
            ],
        ),
        migrations.CreateModel(
            name='JobTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('category', models.CharField(choices=[('Business', 'Business'), ('IT', 'IT'), ('Retail', 'Retail')], default='Business', max_length=200)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.job')),
            ],
        ),
    ]