from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid


'''
Overridden the django's built-in Auth User Model with custom user model,
in which email is required for logging in instead of username.
'''
class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, bio, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            bio = bio
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    profile_pic = models.ImageField(
        'Profile Picture', upload_to='portfol_io/profile_pics', default='portfol_io/profile_pics/default.jpg')
    bio = models.TextField()
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AccountManager()

    TEMPLATE_CHOICES = (
        ('portfolio_template1.html', 'Template 1'),
        ('portfolio_template2.html', 'Template 2'),
        ('portfolio_template3.html', 'Template 3'),
        ('portfolio_template4.html', 'Template 4'),
    )
    portfolio_template = models.CharField('',
                                          max_length=100, choices=TEMPLATE_CHOICES, default='portfolio_template2.html')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# users can add projects to their account
class Project(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    google_cloud_link = models.URLField()

    def __str__(self):
        return self.project_name
