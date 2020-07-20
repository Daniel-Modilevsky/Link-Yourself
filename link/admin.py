from django.contrib import admin
from link.models import LinkDB
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from link.models import Profile


admin.site.register(LinkDB)
admin.site.register(Profile)

