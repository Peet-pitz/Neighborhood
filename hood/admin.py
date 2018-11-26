from django.contrib import admin
from .models import Hood, User, Business, Post, Health, Police


# Register your models here.
admin.site.register(Hood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Health)
admin.site.register(Police)