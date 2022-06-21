from django.contrib import admin
from.models import lastlogin, lastlogout, user
# Register your models here.
admin.site.register(user)
admin.site.register(lastlogin)
admin.site.register(lastlogout)