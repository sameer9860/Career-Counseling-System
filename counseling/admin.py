from django.contrib import admin

from .models import StudentInput


@admin.register(StudentInput)
class StudentInputAdmin(admin.ModelAdmin):
    list_display = ("name", "grades", "interest", "suggestion")
    search_fields = ("name", "interest", "suggestion")
    list_filter = ("interest", "suggestion")

from django.contrib import admin

# Register your models here.
