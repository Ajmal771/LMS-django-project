from django.shortcuts import render,redirect
from .models import Courses
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def add(request):
    if request.method == 'POST':
        c_obj = Courses()
        c_obj.title = request.POST['title']
        c_obj.category = request.POST['category']
        c_obj.description = request.POST['description']
        c_obj.price = request.POST['price']
        c_obj.save()
        return redirect('/')
    return render(request, 'add_form.html')


def course_list(request):
    courses = Courses.objects.all()
    return render(request, "course_list.html", {"courses": courses})

def update(request,id):
    cors_obj = Courses.objects.get(id=id)
    if request.method == 'POST':
        cors_obj = Courses.objects.get(id=id)
        cors_obj.title = request.POST['title']
        cors_obj.category = request.POST['category']
        cors_obj.description = request.POST['description']
        cors_obj.price = request.POST['price']
        cors_obj.save()
        return redirect('/')
    return render(request, 'Update.html', {'data': cors_obj})
