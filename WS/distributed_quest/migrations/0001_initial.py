# Generated by Django 3.0.8 on 2021-01-08 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExam',
            fields=[
                ('universityId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributed_quest.Exam')),
            ],
        ),
    ]