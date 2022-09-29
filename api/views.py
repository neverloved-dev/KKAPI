from getpass import getuser
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
import mailbox
from urllib import response
import smtplib
# Create your views here.

#Admin views
@api_view(["POST"])
def registerUser(request):
    aName = request.data.clean["name"]
    aPassword = request.data.clean["password"]
    aEmail = request.data.clean["email"]
    aFirstName = request.data.clean["f_name"]
    aLast_Name = request.data.clean["l_name"]
    aIsStudent = request.data.clean["is_student"]
    aIsTeacher = request.data.clean["is_teacher"]
    aIsAdmin = request.data.clean["is_admin"]
    aIsSuper = request.data.clean["is_super_admin"]

    user = User()
    user.first_name = aName
    user.last_name = aLast_Name
    user.email = aEmail
    user.password = aPassword
    user.is_admin = aIsAdmin
    user.is_teacher = aIsTeacher
    user.is_student = aIsStudent
    user.is_super_admin = aIsSuper
    user.save()
    return redirect("/profile")


@api_view(["POST"])
def loginUser(request):
   name = request.clean["name"]
   password = request.clean["password"]
   if(name == "" or password == ""):
       return response("Please fill in all fields").json()
   user = authenticate(username = name, password = password)
   if(user == null):
       return response("User not found").json()

   if(user.password == password and user is not None):
       return redirect("/profile")
   else:
       return response("Invalid password")

#Check if user is logged in for these two
@api_view(["GET"])
def getUserProfile(request):
    pass


@api_view(["GET"])
def getStudentData(request,name):
    
    student = Student.object.get(name=name)
    return response(student)


@api_view(["GET"])
def getTeacherData(request,name):
    teacher = Teacher.object.get(name=name)
    return response(teacher)


@api_view(["GET"])
def getBatchData(request,name):
    batch = Batch.object.get(name=name)
    return response(batch)


@api_view(["GET"])
def getCourseData(request,name):
    course = Course.object.get(name=name)
    return response(course)


@api_view(["GET"])
def getTaskData(request,name):
    task = Task.object.get(name=name)
    return response(task)


def sendMail(mail):
    FROM = "mymai@gmail.com"
    TO=mail 
    SUBJECT="User created"
    TEXT="url login:"
    message = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # Send the mail
    server = smtplib.SMTP('myserver')
    server.sendmail(FROM, TO, message)
    server.quit()

@api_view(["POST"])
def createStudent(request):
    name = request.data.clean["name"]
    password = request.data.clean["password"]
    mail = request.data.clean["email"]
    student = Student()
    student.name = name
    student.password = password 
    sendMail(mail)
    return redirect("/")



@api_view(["POST"])
def createTeacher(request):
    name = request.data.clean["name"]
    password = request.data.clean["password"]
    mail = request.data.clean["email"]
    teacher = Teacher()
    teacher.name = name
    teacher.password = password 
    sendMail(mail)
    return redirect("/")


@api_view(["POST"])
def createCourse(request):
    name = request.data.clean["name"]
    teacher = request.data.clean["teacher"]
    course = Course()
    course.name = name
    course.teacher = teacher 
    course.save()
    return redirect("/")




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
    title = request.data.clean["title"]
    text = request.data.clean["text"]
    forum = Forum()
    forum.name = title
    forum.text = text
    forum.save()
    return redirect("/forum")

@api_view(["POST"])
def createClass(request,user:User):
    name = request.data.clean["name"]
    if(user.is_authenticated and user.is_teacher):
        course = Course()
        course.name = name
        course.teacher = user
        course.save()

@api_view(["POST"])
def uploadTutorial(request):
    name = request.data.clean["name"]
    if(user.is_authenticated and user.is_teacher):
        course = Course()
        course.name = name
        course.teacher = user
        course.save()

@ap_view(["POST"])
def postTest(request):
     name = request.data.clean["name"]
     if(user.is_authenticated and user.is_teacher):
        test = Test()
        test.title = title
        test.teacher = user
        test.save()

@api_view(["GET"])
def getAcrivityLists(request):
    pass

@api_view(["GET"])
def getActivityList(request,id):
    pass

@api_view(["GET"])
def viewProfile(request,id):
    user = User.objects.get(id=id)
    return redirect("/profile",{user:user})

@api_view(["PUT"])
def editProfile(request,id):
    user = User.objects.get(id=id)
    user.username = request.data.clean["username"]
    user.f_name = request.data.clean["first name"]
    user.l_name = request.data.clean["last name"]
    user.email = request.data.clean["email"]
    user.save()
    return redirect("profile",{user:user})

@api_view(["POST"]) #ZOOM API
def createMeeting(request):
    pass