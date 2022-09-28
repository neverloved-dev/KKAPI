from django.shortcuts import render
from rest_framework import viewsets
from .models import *
# Create your views here.

#Teacher views
@api_view(["POST"])
def createTask(request):
    name = request.data.clean["name"]
    description = request.data.clean["description"]
    course = request.data.clean["course"]
    task = Task()
    task.name = name
    task.description = description
    task.course = course
    #task.teacher = user.getCurrentUser()
    task.save()

@api_view(["POST"])
def createForum(request):
    pass

@api_view(["POST"])
def createClass(request):
    name = request.data.clean["name"]
    #teacher user.getCurrentUser()
    course = Course()
    course.name = name
    #course.teacher = teacher
    course.save()

@api_view(["POST"])
def uploadTutorial(request):
    pass

@ap_view(["POST"])
def postTest(request):
    pass

@api_view(["GET"])
def getAcrivityLists(request):
    pass

@api_view(["GET"])
def getActivityList(request,id):
    pass

@api_view(["GET"])
def viewProfile(request,id):
    pass

@api_view(["PUT"])
def editProfile(request,id):
    pass

@api_view(["POST"]) #ZOOM API
def createMeeting(request):
    pass