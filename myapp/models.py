from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default="General")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'courses'


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)


class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    question = models.TextField()
    correct_answer = models.CharField(max_length=200)


class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'Register'