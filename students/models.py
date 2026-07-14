from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=18)
    gender = models.CharField(max_length=10, default="Not Specified")

    #Stringify method to return the name of the student
    def __str__(self):
        return self.name
    

