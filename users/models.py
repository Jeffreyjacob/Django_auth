from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


# Create your models here.

class UserManager(BaseUserManager):   
    def create_user(self,email,first_name='',last_name='',password=None):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,first_name,last_name,password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser,PermissionsMixin):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.EmailField(unique=True,max_length=255)
      is_active = models.BooleanField(default=True)
      is_staff = models.BooleanField(default=False)
      is_superuser = models.BooleanField(default=False)
      
      objects = UserManager()
      
      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['first_name','last_name']
      
      def __str__(self):
          return self.email
        



