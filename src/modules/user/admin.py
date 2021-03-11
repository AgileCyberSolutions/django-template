from django.contrib import admin 
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 

# Register your models here.
from .models.user import User as usermodel

class CustomUserAdmin(BaseUserAdmin): 
  fieldsets = ( 
      (None, {'fields': ('email', 'password', )}), 
      (_('Personal info'), {'fields': ('first_name', 'last_name','gender')}), 
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
      (_('user_info'), {'fields': ('phone_no',)})
  ) 
  add_fieldsets = ( 
      (None, { 
          'classes': ('wide', ), 
          'fields': ('email', 'password1', 'password2'), 
      }), 
  ) 
  list_display = ['email', 'first_name', 'last_name', 'is_staff', "phone_no"] 
  search_fields = ('email', 'first_name', 'last_name') 
  ordering = ('email', ) 



admin.site.register(usermodel,CustomUserAdmin)