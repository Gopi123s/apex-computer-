from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.


class Courses(models.Model):
    
    title=models.CharField(max_length=100)
    desc=HTMLField()
    url=models.CharField(max_length=100)
    period_time=models.CharField(max_length=100)
    mode=models.CharField(max_length=50)
    image=models.ImageField(upload_to='courses/')
    date=models.DateTimeField(auto_now=False, auto_now_add=False)
    
# '<img src="/media/{}" style=" width:40px; height:40px; border-radius:50%"/> '.format(self.image)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html("<img src='/media/{}' style='width:40px; height:40px; border-radius:50%'/>".format(self.image))


class Students(models.Model):
    name=models.CharField(max_length=100)
    f_name=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    date=models.DateField(auto_now=False, auto_now_add=False)
    mobile=models.CharField(max_length=10)
    email=models.EmailField()
    image=models.ImageField(upload_to='students/')
    course_enroll=models.ForeignKey(Courses,on_delete=models.CASCADE)

    def image_tag(self):
        return format_html("<img src='/media/{}' style='width:40px; height:40px; border-radius:50%'/>".format(self.image))


    def __str__(self):
        return self.name