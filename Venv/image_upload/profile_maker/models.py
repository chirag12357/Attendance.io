from django.db import models
class User_Profile(models.Model):
    Faculty_Name = models.CharField(max_length=200)
    Lecture_Name = models.CharField(max_length=500)
    Upload_Picture = models.FileField()
    def __str__(self):
        return self.Faculty_Name
