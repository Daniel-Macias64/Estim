# Generated by Django 2.0.3 on 2018-03-12 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionCursos', '0009_auto_20180312_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptos', models.PositiveSmallIntegerField()),
                ('id_enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionCursos.Enrollment')),
            ],
        ),
    ]