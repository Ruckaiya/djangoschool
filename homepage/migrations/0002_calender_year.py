# Generated by Django 3.0.2 on 2020-01-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calender',
            name='year',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
