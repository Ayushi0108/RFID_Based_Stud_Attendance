from django.db import models

# Create your models here.
class Record(models.Model):
    rfid = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    course_code = models.CharField(max_length=10)
    course = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Stud(models.Model):    
    rfid = models.CharField(max_length=30)
    roll = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    def __str__(self):
        return self.name

# class Registration(models.Model):
#     Student = models.ForeignKey(Stud.roll)
#     Course_code = models.CharField(max_length=10)
#     def __str__(self):
#         return "Object"

    


