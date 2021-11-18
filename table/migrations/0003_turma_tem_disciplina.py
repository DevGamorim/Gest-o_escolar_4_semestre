# Generated by Django 3.2.9 on 2021-11-18 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20211118_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='turma_tem_disciplina',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.disciplina')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.turma')),
            ],
        ),
    ]
