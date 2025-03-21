from django.shortcuts import render,redirect
from .models import Courses,Register
# Create your views here.


def home(request):
    courses = Courses.objects.all()[:3]
    user = request.session.get('user')
    if user:
        return render(request, 'home.html', {'data': courses})
    else:
        return redirect('/')


def about(request):
    return render(request, 'about.html')


def add(request):
    if request.method == 'POST':
        c_obj = Courses()
        c_obj.title = request.POST['title']
        c_obj.category = request.POST['category']
        c_obj.description = request.POST['description']
        c_obj.price = request.POST['price']
        c_obj.image = request.FILES['image']
        c_obj.save()
        return redirect('/home')
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
        cors_obj.image = request.FILES['image']
        cors_obj.save()
        return redirect('/home')
    return render(request, 'Update.html', {'data': cors_obj})


def delete(request,id):
    cors_obj = Courses.objects.get(id=id)
    cors_obj.delete()
    return redirect('/home')


def register(request):
    if request.method == 'POST':
        rgst_obj = Register()
        rgst_obj.name = request.POST['name']
        rgst_obj.email = request.POST['email']
        rgst_obj.password = request.POST['password']
        rgst_obj.save()
        return redirect('/home')
    return render(request, 'Registration_form.html')


def login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        user = Register.objects.get(name=name, password=password)
        if user:
            request.session['user'] = user.id
            return redirect('/home')
        else:
            return render(request, 'login_form.html', {'error': 'Invalid username or password'})
    return render(request, 'login_form.html')


def logout(request):
    del request.session['user']
    return redirect('/')

