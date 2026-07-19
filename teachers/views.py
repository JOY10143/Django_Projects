from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher


# Read Operation
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers_crud/teacher_list.html", {
        "teachers": teachers
    })


# Create Operation
def add_teacher(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        subject = request.POST.get("subject")

        Teacher.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            subject=subject
        )

        return redirect("teacher_list")

    return render(request, "teachers_crud/add_teacher.html")


# Update Operation
def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":
        teacher.full_name = request.POST["full_name"]
        teacher.email = request.POST["email"]
        teacher.phone_number = request.POST["phone_number"]
        teacher.subject = request.POST["subject"]

        teacher.save()

        return redirect("teacher_list")

    return render(request, "teachers_crud/edit_teacher.html", {
        "teacher": teacher
    })


# Delete Operation
def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()

    return redirect("teacher_list")