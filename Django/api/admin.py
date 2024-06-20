from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Career)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(FormMonthly)
admin.site.register(FormFinal)

