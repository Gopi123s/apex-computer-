from django.shortcuts import render
from apexweb.models import *
# Create your views here.

def home(request):
    crs=Courses.objects.all()
    stu=Students.objects.all()
    
    print(stu)
    print(crs)
    d={'crs':crs ,'stu':stu}
    return render (request,'home.html',d)


def about(request):
    crs=Courses.objects.all()
    return render(request,'about.html',{'crs':crs})


def post(request,url):
    course=Courses.objects.all()
    crs=Courses.objects.all()
    stu=Students.objects.get(url=url)
    print(stu)
    d={'stu':stu ,'course':course,'crs':crs}
    return render(request,'post.html',d)
    

def category(request,url):
    course=Courses.objects.all()
    crss=Courses.objects.get(url=url)
    crs=Courses.objects.all()
    # stu=Students.objects.all()
    ############
    # cat=Courses.objects.get(url=url)
    stu=Students.objects.filter(course_enroll=crss)
    
    d={'crss':crss ,'course':course,'stu':stu,'crs':crs}
    return render(request,'category.html',d)
