from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from restricted_users.models import User


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
