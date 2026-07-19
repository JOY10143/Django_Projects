from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student


# Home Page
def home(request):
    return render(request, 'home.html')


# About Page
def about(request):
    return render(request, 'about.html')


# Contact Page
def contact(request):
    return render(request, 'contact.html')


def courses(request):
    return HttpResponse("Welcome to the Courses page.")


def services(request):
    return HttpResponse("Welcome to the Services page.")


# Read Operation
def student_list(request):
    students = Student.objects.all()
    return render(request, "students_crud/student_list.html", {"students": students})


# Create Operation
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        course = request.POST.get("course")

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            course=course
        )

        return redirect("student_list")

    return render(request, "students_crud/add_student.html")


# Update Operation
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.email = request.POST["email"]
        student.phone = request.POST["phone"]
        student.course = request.POST["course"]

        student.save()

        return redirect("student_list")

    return render(request, "students_crud/edit_student.html", {
        "student": student
    })


# Delete Operation
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("student_list")