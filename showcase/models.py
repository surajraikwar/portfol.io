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
        'Profile Picture', upload_to='devshowcase/profile_pics', default='devshowcase/profile_pics/default.jpg')
    bio = models.TextField()
    skills = models.TextField(blank=True, null=True, help_text="Comma-separated list of skills")
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AccountManager()

    TEMPLATE_CHOICES = (
        ('showcase_theme1.html', 'Modern Theme'),
        ('showcase_theme2.html', 'Classic Theme'),
        ('showcase_theme3.html', 'Minimal Theme'),
        ('showcase_theme4.html', 'Creative Theme'),
    )
    portfolio_template = models.CharField('Portfolio Theme',
                                          max_length=100, choices=TEMPLATE_CHOICES, default='showcase_theme2.html')

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
    tech_stack = models.CharField(max_length=200, blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    google_cloud_link = models.URLField(blank=True, null=True)  # Made optional
    project_image = models.ImageField(
        'Project Image', upload_to='devshowcase/project_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.project_name
