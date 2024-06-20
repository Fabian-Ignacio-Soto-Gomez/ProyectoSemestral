from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#User Model y Login funcional
class UserViewSet(viewsets.ViewSet):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def list(self, request):
        queryset = User.objects.all()
        serializers = UserSerializer(queryset, many=True)
        return Response(serializers.data)
    
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializers = UserSerializer(user)
        return Response(serializers.data)
    
class LoginViewSet(viewsets.ViewSet):
    serializers_class = LoginUserSerializer

    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                if user.password == password:
                    if user.student:
                        rol = 'est'
                    elif user.teacher:
                        rol = 'prof'
                    elif user.director:
                        rol = 'director'
                    else:
                        return Response({'response':False}, status=200)
                    
                    return Response({'response': True, 'rol':rol}, status=200)
                else:
                    return Response({'response':False}, status=200)
            except User.DoesNotExist:
                return Response({'response':False}, status=200)
        return Response(status=400)


# ============ Vistas del Estudiante ============
    
# [X] Obtención de la información del estudiante del modelo Student
class StudentInfoViewSet(viewsets.ViewSet):
    def create(self, request):
        email = request.data.get('email')
        if email:
            try:
                student = Student.objects.get(email=email)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=200)
            except Student.DoesNotExist:
                return Response({'response': 'Email no encontrado'}, status=400)
        else:
            return Response({'response': 'Email requerido'}, status=400)
 
# [X] GET de la información del estudiante en el modelo Course
class StudentPerCourseViewSet(viewsets.ViewSet):
    def create(self, request):
        rut = request.data.get('rut')
        if rut:
            try:
                studentCourse = Course.objects.get(rut_student=rut)
                serializer = CourseSerializer(studentCourse)                
                return Response(serializer.data, status=200)
            
            except Course.DoesNotExist:
                return Response({'response': 'Rut no encontrado'}, status=400)
        else:
            return Response({'response': 'Rut requerido'}, status=400)
    
# [ ] POST and GET de los archivos subidos por el estudiante para el modelo Document
class DocumentPerStudentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        id_course = self.request.query_params.get('id_course')
        rut = self.request.query_params.get('rut')

        if id_course and rut:
            course = Course.objects.get(rut_student=rut, id_course=id_course)
            return Document.objects.filter(rut=course)
        return super().get_queryset()
    
    # GET de los archivos subidos por el estudiante
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(rut=self.request.data.get('rut'), id_curso=self.request.data.get('id_curso'))

   # POST de algún archivo subido por el estudiante
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'response':True})
        return Response({'response':False})
    
 
 #  ============ Vistas del Profesor  ============


# ============ Vistas del Profesor ============
# [X] Obtención de la información del Curso con rut profesor y id del curso
class TeacherPerCourseStudent(viewsets.ViewSet):
    def create(self, request):
        rut_teacher = request.data.get('rut')
        id_course = request.data.get('id')
        if id_course and rut_teacher:
            try:                
                courseinfo = Course.objects.filter(id_course=id_course, rut_teacher=rut_teacher)
                serializer = CourseSerializer(courseinfo, many=True)
                if not serializer.data:
                    return Response({'response': 'rut del profesor o curso no identificado'},status=400)
                
                return Response(serializer.data, status= 200)
            
            except Course.DoesNotExist:
                return Response({'response': 'rut del profesor o curso no identificado'}, status = 400)
        else:
            return Response({'response': 'Se necesita rut del profesor e identificador del curso'}, status=400)

# [X] Profesor tiene un Post de actualización de los comentarios por cada alumno
class TeacherCommentPerStudent(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        rut_student = request.data.get('rut_student')
        rut_teacher = request.data.get('rut_teacher')
        id_course = request.data.get('id_course')
        comment_num = request.data.get('comment_num')
        comment = request.data.get('comment')

        if rut_student and rut_teacher and id_course:
            try:
                course = Course.objects.get(rut_student=rut_student, rut_teacher=rut_teacher, id_course=id_course)
                if course:
                    if comment_num == '1':
                        course.comentario_1 = comment
                    elif comment_num == '2':
                        course.comentario_2 = comment
                    elif comment_num == '3':
                        course.comentario_3 = comment
                    else:
                        return Response({'response': False}, status=400)
                    
                    course.save()
                    return Response({'response': True}, status=200)
                
            except Course.DoesNotExist:
                return Response({'response': False}, status=400)
                
        return Response({'response': False}, status=400)

# [X] Profesor tiene un PUT de los nota por cada alumno
class TeacherNotaPerStudent(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        rut_student = request.data.get('rut_student')
        rut_teacher = request.data.get('rut_teacher')
        id_course = request.data.get('id_course')
        nota_num = request.data.get('nota_num')
        nota = request.data.get('nota')

        if rut_student and rut_teacher and id_course:
                if int(nota) < 1 or int(nota) > 7:
                    return Response({'response': False}, status=400)
                try:
                    course = Course.objects.get(rut_student=rut_student, rut_teacher=rut_teacher,id_course=id_course)
                    if course:
                        if nota_num == '1':
                            course.nota_1 = nota
                        elif nota_num == '2':
                            course.nota_2 = nota
                        elif nota_num == '3':
                            course.nota_3 = nota
                        else:
                            return Response({'response': False}, status=400)
                        course.save()
                        return Response({'response': True}, status=200)
                except Course.DoesNotExist:
                    return Response({'response': False}, status=400)
                
        return Response({'response': False}, status=400)
    
# [X] Profesor debe POST and GET del Status del estudiante
class TeacherAvancePerStudent(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        rut_student = request.data.get('rut')
        avance_num = request.data.get('num')
        avance = request.data.get('avance')

        if rut_student:
            try:
                student =  Student.objects.get(rut=rut_student)
                if student:
                    if avance_num == '1':
                        student.avance_1 = avance
                    elif avance_num == '2':
                        student.avance_2 = avance
                    elif avance_num == '3':
                        student.avance_3 = avance
                    else:
                        return Response({'response': 'avance no encontrado'}, status=400)
                    student.save()
                    return Response({'response': True}, status=200)
                
            except Student.DoesNotExist:
                return Response({'response': 'estudiante no encontrado'}, status=400)
        return Response({'response': 'rut no encontrado'}, status=400)

class StudentperRut(viewsets.ViewSet):
    def create(self, request):
        rut = request.data.get('rut')
        student = Student.objects.get(rut=rut)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=200)

# [ ] Profesor debe POST and GET de los archivos subidos por él
class DocumentPerStudentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        id_course = self.request.query_params.get('id_course')
        rut = self.request.query_params.get('rut')

        if id_course and rut:
            course = Course.objects.get(rut_teacher=rut, id_course=id_course)
            return Document.objects.filter(rut=course)
        return super().get_queryset()
    
    # GET de los archivos subidos por el profesor
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(rut=self.request.data.get('rut'), id_curso=self.request.data.get('id_curso'))

   # POST de algún archivo subido por el profesor
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'response':True})
        return Response({'response':False})
