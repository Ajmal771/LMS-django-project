from django.shortcuts import render,redirect
from .models import Instructor

# Create your views here.


def instructor_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            existing_email = Instructor.objects.get(email=email)
            return render(request, 'Instructor_register.html', {'error': 'User with this email already exist'})
        except Instructor.DoesNotExist:
            regtr_obj = Instructor()
            regtr_obj.fullname = request.POST.get('fullname')
            regtr_obj.email = request.POST.get('email')
            regtr_obj.phone_no = request.POST.get('phone_no')
            regtr_obj.expertise_area = request.POST.get('expertise_area')
            regtr_obj.password = request.POST.get('password')
            regtr_obj.image = request.FILES.get('image')
            regtr_obj.save()
            return redirect('/instructor/success')
    return render(request, 'Instructor_register.html')


def instructor_success(request):
    return render(request, 'Instructor_success.html')


def instructor_list(request):
    intcr_obj = Instructor.objects.all()
    return render(request, 'Instructors_list.html', {'instructors': intcr_obj})


def instructor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Instructor.objects.get(email=email, password=password)
            request.session['user'] = user.id
            return redirect('/instructor/home')
        except Instructor.DoesNotExist:
            return render(request, 'Instructor_login.html', {'error': 'Invalid email or password'})
    return render(request, 'Instructor_login.html')


def home(request):
    return render(request, 'Instructor_home.html')


def update_profile(request,id):
    rgstr_obj = Instructor.objects.get(id=id)
    if request.method == 'POST':
        rgstr_obj.fullname = request.POST['fullname']
        rgstr_obj.email = request.POST['email']
        rgstr_obj.phone_no = request.POST['phone_no']
        rgstr_obj.expertise_area = request.POST['expertise_area']
        rgstr_obj.password = request.POST['password']
        rgstr_obj.image = request.FILES['image']
        rgstr_obj.save()
        return redirect('/instructor/home')
    return render(request, 'update_profile.html', {'data': rgstr_obj})
