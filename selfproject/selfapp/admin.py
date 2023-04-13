from django.contrib import admin
from selfapp.models import Courses,Department

# Register your models here.
# class DepartmentAdmin(admin.ModelAdmin):
    # list_display = ['name','slug']
    # prepopulated_fields = {'slug':('name',)}
# admin.site.register(Department,DepartmentAdmin)

# class CoursesAdmin(admin.ModelAdmin):
    # list_display = ['name','slug']
    # prepopulated_fields = {'slug':('name',)}
# admin.site.register(Courses,CoursesAdmin)

admin.site.register(Department)
admin.site.register(Courses)

