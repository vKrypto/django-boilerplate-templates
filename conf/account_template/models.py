from django.db import models
from django.utils.translation import pgettext_lazy
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# Create your models here.


class UserManager(BaseUserManager):

    def get_user(self, email):
        email = UserManager.normalize_email(email)
        return self.model(email=email, is_active=True)


class User(AbstractBaseUser):

    email = models.EmailField(unique=True)
    
    USERNAE_FIELD = 'email'
    objects = UserManager()

    class Meta:

        ordering = ('-id',)
        permissions = (

            # ('view_user',
            #  pgettext_lazy('Permission description', 'Can view users')),
            ('edit_user',
             pgettext_lazy('Permission description', 'Can edit users')),

            ('view_group',
             pgettext_lazy('Permission description', 'Can view groups')),
            ('edit_group',
             pgettext_lazy('Permission description', 'Can edit groups')),

            ('view_staff',
             pgettext_lazy('Permission description', 'Can view staff')),
            ('edit_staff',
             pgettext_lazy('Permission description', 'Can edit staff')),

            ('impersonate_user',
             pgettext_lazy('Permission description', 'Can impersonate users'))
        )
