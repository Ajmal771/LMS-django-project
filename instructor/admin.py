from django.contrib import admin
from .models import Instructor
# Register your models here.


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'expertise_area', 'phone_no', 'password', 'image']
    list_filter = ['expertise_area']
    search_fields = ['fullname', 'email']
    readonly_fields = ['phone_no']

    fieldsets = (
        ('Basic Information', {
            'fields': ('fullname', 'email', 'phone_no')
        }),
        ('Professional Details', {
            'fields': ('expertise_area',)
        })
    )