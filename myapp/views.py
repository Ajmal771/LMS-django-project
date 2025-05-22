from django.shortcuts import render,redirect
from .models import Courses,Register, Bookmark, Cart
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


def home(request):
    courses = Courses.objects.all()[:3]
    return render(request, 'home.html', {'data': courses})


def course_page(request, id):
    if 'user' not in request.session:
        return redirect(f'/login/?next=/view_more/{id}')

    course_obj = Courses.objects.get(id=id)
    return render(request, 'course_details_page.html', {'data': course_obj})


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
        email = request.POST['email']
        try:
            existing_user = Register.objects.get(email=email)
            return render(request, 'Registration_form.html', {'error': 'User with this email already exist'})
        except Register.DoesNotExist:
            rgst_obj = Register()
            rgst_obj.name = request.POST['name']
            rgst_obj.email = email
            rgst_obj.password = request.POST['password']
            rgst_obj.save()
            return redirect('/')
    return render(request, 'Registration_form.html')


def login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        try:
            user = Register.objects.get(name=name, password=password)
            request.session['user'] = user.id
            next_url = request.GET.get('next', '/')  # default to /home
            return redirect(next_url)
        except Register.DoesNotExist:
            return render(request, 'login_form.html', {'error': 'Invalid username or password'})
    return render(request, 'login_form.html')


def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/')


def bookmark(request,id):
    if 'user' in request.session:
        user = Register.objects.get(id=request.session['user'])
        print(user)
        course = Courses.objects.get(id=id)
        cart = Bookmark(user=user, course=course)
        cart.save()
        return redirect('/view_bookmark')
    else:
        redirect('/')


def view_bookmark(request):
    if 'user' in request.session:
        cart_obj = Bookmark.objects.filter(user_id=request.session['user'])
        total = 0
        for item in cart_obj:
            total += item.course.price
        return render(request, 'bookmark.html', {'data': cart_obj, 'total': total})
    else:
        return redirect('/')


def remove_bookmark(request, id):
    crt_obje = Bookmark.objects.get(id=id)
    crt_obje.delete()
    return redirect('/view_bookmark')


def cart(request,id):
    if 'user' in request.session:
        user = Register.objects.get(id=request.session['user'])
        print(user)
        course = Courses.objects.get(id=id)
        cart = Cart(user=user, course=course)
        cart.save()
        return redirect('/view_cart')
    else:
        redirect('/')


def view_cart(request):
    if 'user' in request.session:
        cart_obj = Cart.objects.filter(user_id=request.session['user'])
        total = 0
        for item in cart_obj:
            total += item.course.price
        return render(request, 'View_cart.html', {'data': cart_obj, 'total': total})
    else:
        return redirect('/')


def remove_cart(request, id):
    crt_obje = Cart.objects.get(id=id)
    crt_obje.delete()
    return redirect('/view_cart')


def checkout_page(request):
    if 'user' in request.session:
        cart_obj = Cart.objects.filter(user_id=request.session['user'])
        total = 0
        for item in cart_obj:
            total += item.course.price
        return render(request, 'Checkout_page.html', {'data': cart_obj, 'total': total})
    else:
        return redirect('/')


def payment_page(request, id):
    course_obj = Courses.objects.get(id=id)
    return render(request, 'payment_page.html', {'data': course_obj})


def video(request, id):
    video_obj = Courses.objects.get(id=id)
    return render(request, 'video_page.html',{'video': video_obj})


def search_results(request):
    query = request.GET.get('q')
    courses = []

    if query:
        courses = Courses.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'search_results.html', {
        'query': query,
        'courses': courses
    })