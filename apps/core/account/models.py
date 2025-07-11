from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


# user Auth guide I followed
# https://www.youtube.com/watch?v=SFarxlTzVX4&t=883s
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None, ):
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        # user.first_name = first_name
        # user.lastname = last_name
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        app_label = 'account'
        
    email = models.EmailField(unique=True, max_length=200)
    username = models.CharField(max_length=30, unique=True, null=True)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    discord_user_id = models.BigIntegerField(null=True, blank=True, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    can_login = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.email).title()
        # return "{})".format(self.first_name).title()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
