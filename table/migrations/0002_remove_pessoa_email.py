# Generated by Django 3.2.9 on 2021-11-19 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='email',
        ),
    ]