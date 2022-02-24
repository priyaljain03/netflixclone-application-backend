from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
# Create your models here.

MATURITY_CHOICES = (('all', 'All'),
                    ('kids', 'kids'))

def upload_to(instance,filename):
    return 'profiles/{filename}'.format(filename=filename)

class NewUserManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Super User must be assigned to is_staff = True'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser'
            )

        user = self.create_user(
            email, user_name, first_name, last_name, password, **other_fields)
        return user

    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=50, unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now)

    objects = NewUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Profile(models.Model):
    name = models.CharField(max_length=225, blank=False, null=False)
    image = models.ImageField(upload_to=upload_to,default='profiles/default.png')
    maturity_setting = models.CharField(
        max_length=50, choices=MATURITY_CHOICES)
    user = models.ForeignKey(NewUser, blank=False,
                             null=False, on_delete=models.CASCADE)
