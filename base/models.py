from django.db import models

class Course(models.Model):
    courses = (('1st to 7th class','1st to 7th class'),('8th class','8th class'),('10th class','10th class'),('11th Arts','11th Arts'),('11th Science','11th Science'),('12th Arts','12th Arts'),('12th Science','12th Science'))
    
    course_name = models.CharField(choices=courses,max_length=100)
    description = models.TextField()
    fee = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Courses"
    
    def __str__(self):
        return self.course_name
        
class Gallery(models.Model):
    choices = (('Event','Event'),('Result_banner','Result_banner'),('Teacher Banner','Teacher Banner'),)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(choices=choices, max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Galleries"
    
    def __str__(self):
        return self.title
    
class Faculty(models.Model):
    designations = (('Director','Director'),('Faculty Teacher','Faculty Teacher'),('HOD','HOD'),)
    
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='faculty/')
    designation = models.CharField(choices=designations,max_length=100)
    
    class Meta:
        verbose_name_plural = "Faculties"

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
    
    class Meta:
        verbose_name_plural = "Enquiries"

    def __str__(self):
        return f"{self.student_name} - {self.interested_course}"