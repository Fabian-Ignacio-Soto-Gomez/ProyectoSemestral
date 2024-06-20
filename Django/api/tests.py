from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from django.test import TestCase

from .models import *
from .serializers import *
from .views import *

# Create your tests here.
class TestLoginViewSet(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.viewset = LoginViewSet.as_view({'post':'create'})

        self.user = User.objects.create(
            email='test@example.com',
            password='password',
            student=True,
            teacher=False,
            director=False
        )
    
    def test_valid_login(self):
        data = {
            "email": self.user,
            "password": self.user
        }

        request = self.factory.post('/login/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_email(self):
        data = {
            "email": "asda@a.com",
            "password": self.user
        }

        request = self.factory.post('/login/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.data['response'], False)
    
    def test_invalid_password(self):
        data = {
            "email": self.user,
            "password": "as"
        }

        request = self.factory.post('/login/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.data['response'], False)


class TestStudentViewSet(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.viewset = StudentInfoViewSet.as_view({'post':'create'})

        self.user = User.objects.create(
            email='test@example.com',
            password='password',
            student=True,
            teacher=False,
            director=False
        )
        self.career = Career.objects.create(career_name = 'Arquitectura')
        self.student = Student.objects.create(
            rut="12345678",
            email=self.user,
            carrer_id=self.career,
            name='Test Student',
            avance_0=True,
            avance_1=True,
            avance_2=False,
            avance_3=False
        )

    def test_create_valid_email(self):
        valid_email = {'email': self.user.email}
        request = self.factory.post('/student/', data=valid_email)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 200)
    
    def test_create_invalid_email(self):
        invalid_email = {'email': 'ui@shigure.com'}
        request = self.factory.post('/student/', data=invalid_email)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

class TestStudentPerCourseViewSet(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.viewset = StudentPerCourseViewSet.as_view({'post':'create'})

        self.user = User.objects.create(
            email='test@example.com',
            password='password',
            student=True,
            teacher=False,
            director=False
        )
        self.user2 = User.objects.create(
            email='test2@example.com',
            password='password',
            student=False,
            teacher=True,
            director=False
        )

        self.career = Career.objects.create(career_name = 'Arquitectura')

        self.student = Student.objects.create(
            rut = "123123213",
            email = self.user,
            carrer_id = self.career,
            name = 'Test Student',
            avance_0 = True,
            avance_1 = True,
            avance_2 = False,
            avance_3 = False
        )

        self.teacher = Teacher.objects.create(
            rut= "123-1",
            email = self.user2,
            name = "123"
        )

        self.course = Course.objects.create(
            id_course = 'PO',
            rut_student = self.student,
            rut_teacher = self.teacher,
            nota_1 = 1,
            nota_2 = 2,
            nota_3 = 3,
            comentario_1 = '1',
            comentario_2 = '2',
            comentario_3 = '3'
        )
    def test_create_valid_rut(self):
        valid_rut = { "rut": self.student.rut }
        request = self.factory.post('/studentpercourse/', data=valid_rut)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 200)
    
    def test_create_invalid_rut(self):
        invalid_rut = {'rut': '212'}
        request = self.factory.post('/studentpercourse/', data=invalid_rut)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

class TestTeacherPerCourseStudent(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.viewset = TeacherPerCourseStudent.as_view({'post':'create'})
        self.user1 = User.objects.create(
            email='test1@example.com',
            password='password',
            student=False,
            teacher=True,
            director=False
        )
        self.user2 = User.objects.create(
            email='test2@example.com',
            password='password',
            student=True,
            teacher=False,
            director=False
        )
        self.career = Career.objects.create(career_name = 'Arquitectura')

        self.teacher = Teacher.objects.create(
            rut="123123",
            email = self.user1,
            name = 'Alberto Hurtado'
        )
        self.student = Student.objects.create(
            rut="12345678",
            email=self.user2,
            carrer_id=self.career,
            name='Test Student',
            avance_0=True,
            avance_1=True,
            avance_2=False,
            avance_3=False
        )

        self.course = Course.objects.create(
            id_course="ECA",
            rut_student= self.student,
            rut_teacher= self.teacher,
            nota_1 = 1,
            nota_2 = 1,
            nota_3 = 1,
            comentario_1 = '2',
            comentario_2 = 'a',
            comentario_3 = '2'
        )

    def test_valid_rut_and_idcourse(self):
        valid_data = { "rut": self.teacher.rut, "id": self.course.id_course }
        request = self.factory.post('/courseinfo/', data=valid_data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_rut(self):
        invalid_data = {
            'rut': '123',
            'id' : self.course.id_course
        }
        request = self.factory.post('/courseinfo/', data=invalid_data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)
    
    def test_invalid_idcourse(self):
        invalid_data = {
            'rut': self.teacher.rut,
            'id': 'ASD'
        }
        request = self.factory.post('/courseinfo/', data=invalid_data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

class TestTeacherCommentPerStudent(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.viewset = TeacherCommentPerStudent.as_view({'post':'create'})
        self.user1 = User.objects.create(
            email='test1@example.com',
            password='password',
            student=False,
            teacher=True,
            director=False
        )
        self.user2 = User.objects.create(
            email='test2@example.com',
            password='password',
            student=True,
            teacher=False,
            director=False
        )
        self.career = Career.objects.create(career_name = 'Arquitectura')

        self.teacher = Teacher.objects.create(
            rut="111-1",
            email = self.user1,
            name = 'Alberto Hurtado'
        )
        self.student = Student.objects.create(
            rut="2223-1",
            email=self.user2,
            carrer_id=self.career,
            name='Test Student',
            avance_0=True,
            avance_1=True,
            avance_2=False,
            avance_3=False
        )
        self.course = Course.objects.create(
            id_course='ECA',
            rut_student= self.student,
            rut_teacher= self.teacher,
            nota_1 = 1,
            nota_2 = 1,
            nota_3 = 1,
            comentario_1 = '2',
            comentario_2 = 'a',
            comentario_3 = '2'
        )
    def test_valid_comment(self):
        valid_data = {
            "rut_student" : self.student.rut,
            "rut_teacher" : self.teacher.rut,
            "id_course" : self.course.id_course,
            "comment_num" : '1',
            "comment" : "asasdadsa"
        }
        request = self.factory.post('/comment/', data=valid_data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 200)

    def test_invalid_rut_student(self):
        data = {
            "rut_student" : "12",
            "rut_teacher" : self.teacher.rut,
            "id_course" : self.course.id_course,
            "comment_num" : '1',
            "comment" : "asasdadsa"
        }
        request = self.factory.post('/comment/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_rut_teacher(self):
        data = {
            "rut_student" : self.student.rut,
            "rut_teacher" : "123",
            "id_course" : self.course.id_course,
            "comment_num" : '1',
            "comment" : "asasdadsa"
        }
        request = self.factory.post('/comment/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_id_course(self):
        data = {
            "rut_student" : self.student.rut,
            "rut_teacher" : self.teacher.rut,
            "id_course" : "AKA47",
            "comment_num" : '1',
            "comment" : "asasdadsa"
        }
        request = self.factory.post('/comment/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_comment_num(self):
        data = {
            "rut_student" : "12",
            "rut_teacher" : self.teacher.rut,
            "id_course" : self.course.id_course,
            "comment_num" : '511',
            "comment" : "asasdadsa"
        }
        request = self.factory.post('/comment/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_comment(self):
        data = {
            "rut_student" : "12",
            "rut_teacher" : self.teacher.rut,
            "id_course" : self.course.id_course,
            "comment_num" : '1',
        }
        request = self.factory.post('/comment/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

class TestTeacherNotaPerStudent(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.viewset = TeacherNotaPerStudent.as_view({'post':'create'})
        self.user1 = User.objects.create(
            email='test1@example.com',
            password='password',
            student=False,
            teacher=True,
            director=False
        )
        self.user2 = User.objects.create(
            email='test2@example.com',
            password='password',
            student=True,
            teacher=False,
            director=False
        )
        self.career = Career.objects.create(career_name = 'Arquitectura')

        self.teacher = Teacher.objects.create(
            rut="111-1",
            email = self.user1,
            name = 'Alberto Hurtado'
        )
        self.student = Student.objects.create(
            rut="2223-1",
            email=self.user2,
            carrer_id=self.career,
            name='Test Student',
            avance_0=True,
            avance_1=True,
            avance_2=False,
            avance_3=False
        )
        self.course = Course.objects.create(
            id_course='ECA',
            rut_student= self.student,
            rut_teacher= self.teacher,
            nota_1 = 1,
            nota_2 = 1,
            nota_3 = 1,
            comentario_1 = '2',
            comentario_2 = 'a',
            comentario_3 = '2'
        )
    def test_valid_nota(self):
        data = {
            "rut_student": self.student.rut,
            "rut_teacher": self.teacher.rut,
            "id_course": self.course.id_course,
            "nota_num": "1",
            "nota": 7
        }
        request = self.factory.post('/nota/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 200)

    def test_invalid_rut_student(self):
        data = {
            "rut_student": "aaa",
            "rut_teacher": self.teacher.rut,
            "id_course": self.course.id_course,
            "nota_num": "1",
            "nota": 7
        }
        request = self.factory.post('/nota/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_rut_techer(self):
        data = {
            "rut_student": self.student.rut,
            "rut_teacher": "aa",
            "id_course": self.course.id_course,
            "nota_num": "1",
            "nota": 7
        }
        request = self.factory.post('/nota/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_id_course(self):
        data = {
            "rut_student": self.student.rut,
            "rut_teacher": self.teacher.rut,
            "id_course": "self.course.id_course",
            "nota_num": "1",
            "nota": 7
        }
        request = self.factory.post('/nota/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_nota_num(self):
        data = {
            "rut_student": self.student.rut,
            "rut_teacher": self.teacher.rut,
            "id_course": self.course.id_course,
            "nota_num": "111",
            "nota": 7
        }
        request = self.factory.post('/nota/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_nota(self):
        data = {
            "rut_student": self.student.rut,
            "rut_teacher": self.teacher.rut,
            "id_course": self.course.id_course,
            "nota_num": "1",
            "nota": 111
        }
        request = self.factory.post('/nota/', data=data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

class TestTeacherAvancePerStudent(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.viewset = TeacherAvancePerStudent.as_view({'post':'create'})
        self.user1 = User.objects.create(
            email='test1@example.com',
            password='password',
            student=False,
            teacher=True,
            director=False
        )
        self.user2 = User.objects.create(
            email='test2@example.com',
            password='password',
            student=True,
            teacher=False,
            director=False
        )
        self.career = Career.objects.create(career_name = 'Arquitectura')

        self.teacher = Teacher.objects.create(
            rut="111-1",
            email = self.user1,
            name = 'Alberto Hurtado'
        )
        self.student = Student.objects.create(
            rut="2223-1",
            email=self.user2,
            carrer_id=self.career,
            name='Test Student',
            avance_0=True,
            avance_1=True,
            avance_2=False,
            avance_3=False
        )
        self.course = Course.objects.create(
            id_course='ECA',
            rut_student= self.student,
            rut_teacher= self.teacher,
            nota_1 = 1,
            nota_2 = 1,
            nota_3 = 1,
            comentario_1 = '2',
            comentario_2 = 'a',
            comentario_3 = '2'
        )
    def test_valid_data(self):
        data = {
            "rut": self.student.rut,
            "num": "1",
            "avance": True
        }
        request = self.factory.post('/avance/', data= data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 200)

    def test_invalid_rut_student(self):
        data = {
            "rut": "as",
            "num": "1",
            "avance": True
        }
        request = self.factory.post('/avance/', data= data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_avance_num(self):
        data = {
            "rut": self.student.rut,
            "num": "12",
            "avance": True
        }
        request = self.factory.post('/avance/', data= data)
        response = self.viewset(request)
        self.assertEqual(response.status_code, 400)