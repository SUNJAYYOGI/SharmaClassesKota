from django.shortcuts import render, redirect
from .models import Course, Notice, Enquiry

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        
        Enquiry.objects.create(student_name=name, phone_number=phone, interested_course=course)
        return redirect('/') 

    courses = Course.objects.all()
    notices = Notice.objects.filter(is_active=True).order_by('-date_posted') 

    context = {
        'courses': courses,
        'notices': notices,
    }
    
    return render(request, 'base/index.html', context)