# Generated by Django 3.2.8 on 2021-10-16 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(verbose_name='Create Date')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_desc', models.CharField(max_length=200)),
                ('task_start', models.DateTimeField(verbose_name='Start Date')),
                ('task_end', models.DateTimeField(verbose_name='End Date')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.person')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_desc', models.CharField(max_length=200)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.task')),
            ],
        ),
    ]