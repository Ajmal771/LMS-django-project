from django.db import models

# Create your models here.


class Instructor(models.Model):
    EXPERTISE_CHOICES = [
        ('technology', 'Technology & Programming'),
        ('business', 'Business & Finance'),
        ('design', 'Design & Creative'),
        ('marketing', 'Marketing & Sales'),
        ('health', 'Health & Fitness'),
        ('language', 'Language Learning'),
        ('other', 'Other'),
    ]
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    expertise_area = models.CharField(max_length=50, choices=EXPERTISE_CHOICES)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        db_table = 'Instructor_register'
