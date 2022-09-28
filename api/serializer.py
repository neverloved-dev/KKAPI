from rest_framework import serializers
from .models import Student, Teacher, Course,Batch 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CourseSerializer(serializer.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch 
        fields = "__all__"
