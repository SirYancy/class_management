from django.contrib import admin
from attendance.models import Student, Class, Session


class ClassAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': [('class_id', 'name'), ('semester', 'year')]
        }),
    )
    list_display = ('class_id', 'name',)
    list_filter = ['class_id', 'name']
    search_fields = ['enrolled_class', 'last_name', 'student_id']


class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'enrolled_class',)
    list_filter = ['enrolled_class', ]


class SessionAdmin(admin.ModelAdmin):
    list_display = ('date',)


admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Session, SessionAdmin)
