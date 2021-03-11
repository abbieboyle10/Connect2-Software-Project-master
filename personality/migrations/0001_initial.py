# Generated by Django 3.1.4 on 2021-03-11 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=120)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='duration of the quiz in minutes')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_score', models.FloatField()),
                ('i_score', models.FloatField()),
                ('n_score', models.FloatField()),
                ('s_score', models.FloatField()),
                ('t_score', models.FloatField()),
                ('f_score', models.FloatField()),
                ('p_score', models.FloatField()),
                ('j_score', models.FloatField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.employee')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personality.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(blank=True, choices=[('e', 'e'), ('i', 'i'), ('n', 'n'), ('s', 's'), ('f', 'f'), ('t', 't'), ('j', 'j'), ('p', 'p')], max_length=200)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personality.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_letter', models.CharField(max_length=200)),
                ('second_letter', models.CharField(max_length=200)),
                ('third_letter', models.CharField(max_length=200)),
                ('fourth_letter', models.CharField(max_length=200)),
                ('person_type', models.CharField(max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('correct', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personality.question')),
            ],
        ),
    ]
