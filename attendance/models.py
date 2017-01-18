from django.conf import settings
from django.db import models
import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Class(models.Model):
    """
    Models a class with a list of students
    """
    SPRING = 0
    FALL = 1

    SEMESTERS = (
        (SPRING, 'Spring'),
        (FALL, 'Fall')
    )

    semester = models.SmallIntegerField(choices=SEMESTERS)
    year = models.IntegerField()
    class_id = models.CharField(max_length=12)
    name = models.CharField(max_length=30)
    enrolled_students = models.ManyToManyField('Student', blank=True)

    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.class_id + ' ' + str((self.SEMESTERS[self.semester])[1]) + ' ' + str(self.year)


class Student(models.Model):
    """
    Each student must sign in as a 'user' sort of each day
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.student_id + ' ' + self.last_name


class Session(models.Model):
    """
    One of these for each day of the term
    """
    date = models.DateField(default=datetime.date.today)
    password = models.CharField(max_length=16)
    session_class = models.ForeignKey(Class)
    students_present = models.ManyToManyField(Student, blank=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Token.objects.create(user=instance)
