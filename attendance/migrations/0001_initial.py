# Generated by Django 3.0.2 on 2020-01-02 19:42

import attendance.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('9 Boys Section 1', 'Class 9'), ('10 Boys Section 1', 'Class 10'), ('10 Boys Section 2', 'Class 10'), ('11 Boys Section 1', 'Class 11'), ('11 Boys Section 2', 'Class 11'), ('12 Boys Section 1', 'Class 12'), ('12 Boys Section 2', 'Class 12')], max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Class 9', 'Class 9'), ('Class 10', 'Class 10'), ('Class 11', 'Class 11'), ('Class 12', 'Class 12')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
            bases=(attendance.models.NamableModel, models.Model),
        ),
        migrations.CreateModel(
            name='Teacher22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
            bases=(attendance.models.NamableModel, models.Model),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Classroom')),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
            bases=(attendance.models.NamableModel, models.Model),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(default=models.DateTimeField(auto_now_add=True))),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Classroom')),
                ('students', models.ManyToManyField(related_name='attendances', to='attendance.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Teacher')),
            ],
        ),
    ]
