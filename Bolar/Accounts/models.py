from queue import Empty
from random import randint
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")

        user_obj = self.model(
            email = self.normalize_email(email),
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user
    

class User(AbstractBaseUser):
    email       = models.EmailField(unique=True, max_length=128, verbose_name="Email")
    username    = models.PositiveIntegerField(unique=True, default=10000)

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date Joined")
    last_login  = models.DateTimeField(auto_now=True, verbose_name="Last Online")

    active      = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)

    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            # New user, assign the next available username
            last_user = User.objects.order_by('-username').first()
            if last_user:
                self.username = last_user.username + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.username)

    def formated_date_joined(self):
        date = self.date_joined
        return date.strftime("%d %b %y om %H:%M")

    def formated_last_login(self):
        date = self.last_login
        return date.strftime("%d %b %y om %H:%M")


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


