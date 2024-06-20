from django.urls import path, include
from api import views
from .views import *
from rest_framework.routers import DefaultRouter

#UserViewSet Router
routerUser = DefaultRouter()
routerUser.register('', UserViewSet, basename='user')

#Login Router
routerLogin = DefaultRouter()
routerLogin.register('', LoginViewSet, basename='login')

# ====== Views Estudiante ====== 
routerInfoStudent = DefaultRouter()
routerInfoStudent.register('', StudentInfoViewSet, basename="info-student")

routerInfoCoursePerStudent = DefaultRouter()
routerInfoCoursePerStudent.register('', StudentPerCourseViewSet, basename='info-course-student')

# ====== Views Profesor ======
routerTeacherPerCourseStudent = DefaultRouter()
routerTeacherPerCourseStudent.register('', TeacherPerCourseStudent, basename='course-info')

routerTeacherComment = DefaultRouter()
routerTeacherComment.register('', TeacherCommentPerStudent, basename='teacher-comment')

routerTeacherNote = DefaultRouter()
routerTeacherNote.register('', TeacherNotaPerStudent, basename='teacher-note')

routerTeacherAvance = DefaultRouter()
routerTeacherAvance.register('', TeacherAvancePerStudent, basename='teacher-avance')

routerStudentperTeacher = DefaultRouter()
routerStudentperTeacher.register('', StudentperRut, basename='student-info')

urlpatterns = [
    # path('upload/', include(routerDocument.urls)),
    path('user/', include(routerUser.urls)),
    path('login/', include(routerLogin.urls)),
    path('student/', include(routerInfoStudent.urls)),
    path('studentpercourse/', include(routerInfoCoursePerStudent.urls)),
    path('courseinfo/', include(routerTeacherPerCourseStudent.urls)),
    path('comment/', include(routerTeacherComment.urls)),
    path('nota/', include(routerTeacherNote.urls)),
    path('avance/', include(routerTeacherAvance.urls)),
    path('infostudent/', include(routerStudentperTeacher.urls))
]
