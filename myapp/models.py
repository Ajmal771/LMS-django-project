from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default="General")
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)

    class Meta:
        db_table = 'courses'


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'lessons'


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)


class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    question = models.TextField()
    correct_answer = models.CharField(max_length=200)