from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fee = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Enquiry(models.Model):
    student_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    interested_course = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.interested_course}"