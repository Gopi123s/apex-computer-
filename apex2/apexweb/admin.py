from django.contrib import admin
from .models  import*
# Register your models here.


# config  object to admin panel 

class CoursesAdmin(admin.ModelAdmin):
    list_display=('title','desc','url','image_tag')
    search_fields=('title',)


class StudentsAdmin(admin.ModelAdmin):
    list_display=('name','f_name','mobile','email','course_enroll','image_tag','url')
    search_fields=('name',)

admin.site.register(Courses , CoursesAdmin)
admin.site.register(Students,StudentsAdmin)