from django.contrib import admin
from .models import Course, Notice, Enquiry, Gallery, Faculty, Video

admin.site.register(Notice)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'fee', 'description')
    search_fields = ('course_name', 'fee', 'description')
    list_filter = ('course_name',)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'phone_number', 'interested_course', 'date')
    search_fields = ('student_name', 'phone_number')
    
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'category', 'date', 'is_visible')
    list_editable = ('is_visible',)
    list_filter = ('category', 'is_visible')
    search_fields = ('title', 'category')
    
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name','designation','subject','image')
    search_fields = ('name','designation','subject')
    
@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'video_url')
    search_fields = ('video_title',)
