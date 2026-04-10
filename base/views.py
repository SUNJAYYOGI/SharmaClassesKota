from django.shortcuts import render, redirect
from .models import Course, Notice, Enquiry, Gallery, Faculty

def home(request):
    if request.method == "POST":
        # Yahan exact wahi naam aana chahiye jo HTML ke 'name' attribute mein hai
        name = request.POST.get('student_name')
        phone = request.POST.get('phone_number')
        course_name = request.POST.get('interested_course')
        
        # PRO TIP FIX: Ye 'if' condition lagana zaroori hai.
        # Ye check karega ki teeno inputs aaye hain, tabhi save karega, warna error nahi dega.
        if name and phone and course_name:
            Enquiry.objects.create(
                student_name=name, 
                phone_number=phone, 
                interested_course=course_name
            )
        
        return redirect('home')

    # Baaki tera purana data nikalne ka code waise hi rahega
    courses = Course.objects.all()
    notices = Notice.objects.filter(is_active=True).order_by('-date_posted')
    gallery_images = Gallery.objects.filter(is_visible=True).order_by('-date')[:12]
    faculties = Faculty.objects.all()

    context = {
        'courses': courses,
        'notices': notices,
        'gallery_images': gallery_images,
        'faculties': faculties,
    }
    
    return render(request, 'base/index.html', context)