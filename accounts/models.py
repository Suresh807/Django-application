from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',  # This is referring to the default Group model in auth app
        related_name='customuser_set',  # Custom related_name to avoid conflict with auth.User
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',  # Referring to the default Permission model in auth app
        related_name='customuser_permissions',  # Custom related_name to avoid conflict with auth.User
        blank=True
    )

    # Add any additional custom fields if needed.
