from django.contrib import admin
from .models import Instructor, Course, Lesson

# Instructor modelini admin paneliga qo'shish
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'specialty')
    search_fields = ('name', 'email')

# Course modelini admin paneliga qo'shish
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'instructor')
    list_filter = ('instructor', 'start_date', 'end_date')
    search_fields = ('title', 'description')

# Lesson modelini admin paneliga qo'shish
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title', 'content')

# Register your models here.
