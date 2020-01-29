from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    '''
    Custom user model, inheriting from AbstractUser
    '''
    pass

    def __str__(self):
        # Returns a username on call
        return self.username
