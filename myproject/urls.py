"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('view_more/<int:id>/', views.course_page),
    path('about/', views.about),
    path('add/', views.add),
    path('course_list/', views.course_list),
    path('update/<int:id>', views.update),
    path('delete/<int:id>/', views.delete),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('bookmark/<int:id>/', views.bookmark),
    path('view_bookmark/', views.view_bookmark),
    path('remove_bookmark/<int:id>/', views.remove_bookmark),
    path('add_cart/<int:id>/', views.cart),
    path('view_cart/', views.view_cart),
    path('remove_cart/<int:id>/', views.remove_cart),
    path('checkout_page/', views.checkout_page),
    path('payment_page/<int:id>/', views.payment_page),
    path('video/<int:id>', views.video),
    path('search/', views.search_results, name='search_results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
