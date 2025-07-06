from django.urls import path
from instructor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.instructor_register),
    path('success/', views.instructor_success),
    path('list/', views.instructor_list),
    path('login/', views.instructor_login),
    path('home/', views.home),
    path('update_profile/<int:id>/', views.update_profile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)