# Generated by Django 5.1.6 on 2025-03-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_courses_created_at_remove_courses_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='category',
            field=models.CharField(default='General', max_length=200),
        ),
    ]
