# Generated by Django 5.0.4 on 2024-06-20 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_carrer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFinal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut_evaluador', models.CharField(max_length=100)),
                ('nota', models.IntegerField()),
                ('comentarios', models.CharField(max_length=1000)),
                ('rut_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rut_empresa_form_final', to='api.company')),
                ('rut_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rut_estudiante_form_final', to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='FormMonthly',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nota', models.IntegerField()),
                ('comentarios', models.CharField(max_length=1000)),
                ('rut_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rut_empresa_form_mensual', to='api.company')),
                ('rut_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rut_estudiante_form_mensual', to='api.student')),
            ],
        ),
    ]