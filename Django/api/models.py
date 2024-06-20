from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=200)
    student = models.BooleanField()
    teacher = models.BooleanField()
    director = models.BooleanField()

    def __str__(self):
        return self.email

class Career(models.Model):
    carrer_id = models.AutoField(primary_key=True)
    career_name = models.CharField(max_length=50)

    def __str__(self):
        return self.career_name

class Student(models.Model):
    rut = models.CharField(primary_key=True, max_length=100)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_email")
    carrer_id = models.ForeignKey(Career, on_delete=models.CASCADE, related_name="student_carrera_id")
    name = models.CharField(max_length=50, null=True)
    avance_0 = models.BooleanField()
    avance_1 = models.BooleanField()
    avance_2 = models.BooleanField()
    avance_3 = models.BooleanField()

    def __str__(self):
        return self.rut

class Company(models.Model):
    id_company = models.AutoField(primary_key=True)
    rut_student = models.OneToOneField(Student, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField()
    rut_supervisor = models.CharField(max_length=100)
    name_supervisor = models.CharField(max_length=50)
    email_supervisor = models.EmailField()

    def __str__(self):
        return self.rut_supervisor

class Teacher(models.Model):
    rut = models.CharField(primary_key=True, max_length=100)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="techer_email")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.rut
    
class Course(models.Model):
    id_course = models.CharField(max_length=10)
    rut_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="rut_student")
    rut_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="rut_teacher")
    nota_1 = models.FloatField()
    nota_2 = models.FloatField()
    nota_3 = models.FloatField()
    comentario_1 = models.CharField(max_length=1000)
    comentario_2 = models.CharField(max_length=1000)
    comentario_3 = models.CharField(max_length=1000)

    def __str__(self):
        return self.id_course

class Document(models.Model):
    id_curso = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="id_curso_document")
    rut = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    date_upload = models.DateTimeField()
    avance_1 = models.BooleanField()
    avance_2 = models.BooleanField()
    avance_3 = models.BooleanField()

    def __str__(self):
        return self.file

class FormMonthly(models.Model):
    id = models.AutoField(primary_key=True)
    rut_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='rut_estudiante_form_mensual')
    rut_empresa = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='rut_empresa_form_mensual')
    nota = models.IntegerField()
    comentarios = models.CharField(max_length=1000)

    def __str__(self):
        return self.id

class FormFinal(models.Model):
    id = models.AutoField(primary_key=True)
    rut_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='rut_estudiante_form_final')
    rut_empresa = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='rut_empresa_form_final')
    rut_evaluador = models.CharField(max_length=100)
    nota = models.IntegerField()
    comentarios = models.CharField(max_length=1000)

    def __str__(self):
        return self.id
