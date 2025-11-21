from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Optional biography text for the user
    bio = models.TextField(blank=True, null=True)

    # Optional profile image stored in 'avatars/' folder
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # Fix for reverse accessor clashes
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # جلوگیری از clash با auth.User.groups
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # جلوگیری از clash با auth.User.user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username
