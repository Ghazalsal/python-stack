# Generated by Django 2.2.4 on 2021-05-20 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='age',
        ),
    ]