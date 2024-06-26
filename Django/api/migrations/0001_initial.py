# Generated by Django 5.0.4 on 2024-06-15 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('carrer_id', models.AutoField(primary_key=True, serialize=False)),
                ('career_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_course', models.CharField(max_length=10)),
                ('nota_1', models.FloatField()),
                ('nota_2', models.FloatField()),
                ('nota_3', models.FloatField()),
                ('comentario_1', models.CharField(max_length=1000)),
                ('comentario_2', models.CharField(max_length=1000)),
                ('comentario_3', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('rut', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
                ('student', models.BooleanField()),
                ('teacher', models.BooleanField()),
                ('director', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('date_upload', models.DateTimeField()),
                ('avance_1', models.BooleanField()),
                ('avance_2', models.BooleanField()),
                ('avance_3', models.BooleanField()),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_curso_document', to='api.course')),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rut', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('avance_0', models.BooleanField()),
                ('avance_1', models.BooleanField()),
                ('avance_2', models.BooleanField()),
                ('avance_3', models.BooleanField()),
                ('carrer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_carrera_id', to='api.career')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_email', to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='rut_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rut_student', to='api.student'),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id_company', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('rut_supervisor', models.CharField(max_length=100)),
                ('name_supervisor', models.CharField(max_length=50)),
                ('email_supervisor', models.EmailField(max_length=254)),
                ('rut_student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='rut_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rut_teacher', to='api.teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='techer_email', to='api.user'),
        ),
    ]
