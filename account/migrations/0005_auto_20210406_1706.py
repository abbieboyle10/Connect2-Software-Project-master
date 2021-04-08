# Generated by Django 3.1.4 on 2021-04-06 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210406_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=200)),
                ('years_of', models.CharField(blank=True, choices=[('1 year <', '1 year <'), ('1 - 2 years', '1 - 2 years'), ('2 - 5 years', '2 - 5 years'), ('5 - 10 years', '5 - 10 years'), ('10+ years', '10+ years')], max_length=200)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.employee')),
            ],
        ),
        migrations.CreateModel(
            name='JobSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=200)),
                ('years_of', models.CharField(blank=True, choices=[('1 year <', '1 year <'), ('1 - 2 years', '1 - 2 years'), ('2 - 5 years', '2 - 5 years'), ('5 - 10 years', '5 - 10 years'), ('10+ years', '10+ years')], max_length=200)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.job')),
            ],
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('interview', 'interview'), ('second round', 'second round'), ('rejected', 'rejected'), ('applied', 'applied')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]