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
            regtr_obj.save()
            return redirect('/')
    return render(request, 'Instructor_register.html')