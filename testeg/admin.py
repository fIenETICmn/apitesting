from django.contrib import admin
from .models import User, Product, Category

# Register your models here.

class UserAdmin(admin.ModelAdmin):

    list_display = ['email']

admin.site.register(User,UserAdmin)

admin.site.register(Product)
admin.site.register(Category)
