from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, ProfileContact, Communities


class UserInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Additional information'
    
class ContactsInline(admin.StackedInline):
    model = ProfileContact
    can_delete = True
    verbose_name_plural = 'Contacts'
    
class CommunitiesInline(admin.StackedInline):
    model = Communities
    can_delete = True
    verbose_name_plural = 'Communities'
 

class UserAdmin(UserAdmin):
    inlines = (UserInline, ContactsInline, CommunitiesInline, )
 

admin.site.unregister(User)
admin.site.register(User, UserAdmin)