from django.contrib import admin
from .models import Course, Notice, Enquiry

admin.site.register(Course)
admin.site.register(Notice)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'phone_number', 'interested_course', 'date')
    search_fields = ('student_name', 'phone_number')