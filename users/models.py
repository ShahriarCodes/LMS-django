from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# admin can not be created from createsuperuser
# as student and teacher cannot be null
# create admin from shell
class User(AbstractUser):
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str_(self):
        return self.user.username
