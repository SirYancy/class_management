"""Class-based Admin settings


Included:
* ClassAdmin
  * For administering individual classes
* StudentAdmin
  * For administering individual students
* SessionAdmin
  * For administering individual class sessions
"""

from django.contrib import admin
from attendance.models import Student, Class, Session


class ClassAdmin(admin.ModelAdmin):
    """ClassAdmin - Sets up admin page for Classes

    Basic info:
    * Major fields are class_id, name, semester, year
    * displays in list only class_id and name
    * Can filter by class_id and name
    * Can search by students enrolled, by last name and student id.
    """
    fieldsets = (
        (None, {
            'fields': [('class_id', 'name'), ('semester', 'year'), 'enrolled_students', ]
        }),
    )
    list_display = ('class_id', 'name',)
    list_filter = ['class_id', 'name']
    search_fields = ['enrolled_classes', 'last_name', 'student_id']


class StudentAdmin(admin.ModelAdmin):
    """StudentAdmin - Sets up admin page for Students

    Basic Info:
    * Displayed in list are last_name, first_name, enrolled_class, and student_id
    * Can filter by enrolled_class
    """
    list_display = ('last_name', 'first_name', 'student_id')


class SessionAdmin(admin.ModelAdmin):
    """SessionAdmin - Sets up admin page for Sessions

    Basic Info:
    * Displayed in list: date, session_class, is_open
    * Editable in list: is_open
    * Filterable: session_class
    * Ordered by: date
    """
    list_display = ('date', 'session_class', 'is_open',)
    list_editable = ('is_open',)
    list_filter = ['session_class']
    ordering = ('-date',)


admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Session, SessionAdmin)
