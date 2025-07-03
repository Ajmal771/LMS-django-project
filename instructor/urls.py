from django.urls import path
from instructor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.instructor_register)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)