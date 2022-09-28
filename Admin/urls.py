from datetime import datetime
from django.urls import path,include
from .views import *

urlpatterns = [
        path("/register/admin",registerAdmin),
        path("/register/super",registerSuper),
        path("/login/super",loginSuper),
        path("login/admin",loginAdmin),
        path("/profile/super",getDataSuper),
        path("/profile/admin",getData),
        path("/data/student/<str:name>",getStudentData),
        path("/data/teacher/<str:name>",getTeacherData),
        path("/data/batch/<str:name>",getBatchData),
        path("/data/course/<str:name>",getCourseData),
        path("/data/task/<str:name>",getTaskData),
        path("/data/student/create",createStudent),
        path("/data/teacher/create",createTeacher),
        path("/data/course/create",createCourse)
    ]
