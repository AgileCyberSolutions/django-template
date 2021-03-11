from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils.translation import ugettext_lazy as _ 
from django.conf import settings 
from datetime import date 

# https://www.geeksforgeeks.org/creating-custom-user-model-using-abstractuser-in-django_restframework/
# https://hashedin.com/blog/configure-role-based-access-control-in-django/

class User(AbstractUser): 
  first_name = models.CharField(max_length = 100, blank = False, null = True) 
  last_name = models.CharField(max_length = 100, blank = False, null = True)
  email = models.EmailField(unique = True) 
  password = models.CharField(max_length = 500, blank = False, null = True)
  phone_no = models.CharField(max_length = 10) 
  gender= models.CharField(max_length = 100, blank = False, null = True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username','first_name', 'last_name']



